#!/bin/bash

# $DATA_DIR = diretório onde estão ou serão baixados os arquivos BRBRASIL.zip e estadofisico.csv (Padrão é /tmp)
# 
# 1) Antes Defina as permissoes de seguranca para o MySQL:
#	sudo nano /etc/apparmor.d/usr.sbin.mysqld ->
#		Coloque depois de "/run/mysqld/mysqld.sock w," essas duas linhas:
#		$DATA_DIR/ r,
#		$DATA_DIR/** rw,
#	sudo /etc/init.d/apparmor restart
#	sudo service mysql restart
# 2) Crie uma base de dados com o nome 'acidentes_rodovias' e coloque o collation dele como utf8_bin
# 3) Caso já tenha os arquivos BRBRASIL.zip e estadofisico.csv baixados, comente as linhas que dão 'wget' neles e coloque os arquivos em $DATA_DIR
# 4) Execute o programa:
#	Uso: ./extract-transform-load.sh <BD_USER> <BD_PASS> <DATA_DIR>
#	Ex: ./extract-transform-load.sh root 123456 /tmp

# TODO: - Fazer um log
#		- Receber parametros para definir quais operacoes serao feitas (so extrair? so transformar? so carregar? tudo junto?)
#		- Verificar conexao com a internet caso queira baixar os arquivos

DB_USER=$1
DB_PASS=$2
DATA_DIR=$3

function prepare_enviroment {
	echo -e "\nDownloading data..."
	wget -P $DATA_DIR http://repositorio.dados.gov.br/transportes-transito/transito/BRBRASIL.zip
	wget -P $DATA_DIR https://dl.dropboxusercontent.com/u/18364240/estadofisico.csv

	if [[ ! -f "$DATA_DIR/BRBRASIL.zip" || ! -f "$DATA_DIR/estadofisico.csv" ]]
	then
		echo "ERROR: Files $DATA_DIR/BRBRASIL.zip or $DATA_DIR/estadofisico.csv dont exist"
		exit -1
	fi

	echo -e "\nUnziping data..."
	unzip -o -d $DATA_DIR $DATA_DIR/BRBRASIL.zip
	for i in $(ls $DATA_DIR/BRBRASIL/*.zip)
	do 
		unzip -o -d $DATA_DIR/BRBRASIL $i
	done
	cp -f $DATA_DIR/estadofisico.csv $DATA_DIR/BRBRASIL
	rm -f $DATA_DIR/BRBRASIL/*.zip $DATA_DIR/BRBRASIL/*.pdf

	echo -e "\nStandardizing delimiters..."
	sed -i 's/|/;/g' "$DATA_DIR/BRBRASIL/veiculo.csv"
	sed -i 's/|/;/g' "$DATA_DIR/BRBRASIL/ocorrenciaveiculo.csv"

	echo -e "\nStandardizing null cells to \N..."
	for i in $(ls $DATA_DIR/BRBRASIL/**/*.csv)
	do 
	 	sed -i 's/(null)/\\N/g' $i
		sed -i 's/;;/;\\N;/g' $i
	 	sed -i 's/;\s\+;/;\\N;/g' $i
	 	sed -i 's/;\\ ;/;\\N;/g' $i
	done
	for i in $(ls $DATA_DIR/BRBRASIL/*.csv)
	do 
		sed -i 's/(null)/\\N/g' $i
	 	sed -i 's/;;/;\\N;/g' $i
	 	sed -i 's/;\s\+;/;\\N;/g' $i
		sed -i 's/;\\ ;/;\\N;/g' $i
	done	
}

function prepare_db {
	if [[ ! -f "$(dirname $0)/db-schema.sql" ]]
	then
		echo "ERROR: File $(dirname $0)/db-schema.sql dont exist"
		exit -1
	fi

	echo -e "\nLoading database schema..."
	mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias < $(dirname $0)/db-schema.sql
	if [[ "$?" -ne "0" ]]
	then
		exit -1
	fi
}

function load_domain_data {
	for TABLE in corveiculo localbr estadofisico marcadeveiculo municipio ocorrenciaveiculo #tipoAcidente tipoApreensao tipoAreaEspecial tipoComunicacao tipocrime tipodetencao tipodocumento tipoenvolvido tipolocalidade tipoobra tipopontomedico tipopontonotavel tiporeceptor tiposinalizacao tipounidadeoperacional tipoveiculo uf unidadeoperacional veiculo
	do
		echo -e "\nLoading domain table \"$TABLE\" data..."
		ARQUIVO="$DATA_DIR/BRBRASIL/$TABLE.csv"
		mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "LOAD DATA INFILE '$ARQUIVO' INTO TABLE \`$TABLE\` CHARACTER SET utf8 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES;"
	done
}

function load_semiannual_data {
	ACTUAL_MONTH=$(date +"%m")
	ACTUAL_MONTH=${ACTUAL_MONTH#0}
	ACTUAL_YEAR=$(date +"%Y")
	
	[[ "$ACTUAL_MONTH" -gt "6" ]] && LAST_YEAR_LOAD=$ACTUAL_YEAR || LAST_YEAR_LOAD=$(($ACTUAL_YEAR-1))

	for TABLE in ocorrencia pessoa ocorrenciaacidente ocorrenciaPessoa
	do
		echo -e "\nLoading semiannual table \"$TABLE\" data..."
		for ((YEAR=2007;YEAR<LAST_YEAR_LOAD;YEAR++))
		do
			FILE_HALF_1="$DATA_DIR/BRBRASIL/brbrasil_1_semestre_$YEAR/${TABLE}_1_Semestre_$YEAR.csv"
			FILE_HALF_2="$DATA_DIR/BRBRASIL/brbrasil_2_semestre_$YEAR/${TABLE}_2_Semestre_$YEAR.csv"
			echo "Loading file $FILE_HALF_1"
			mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "LOAD DATA INFILE '$FILE_HALF_1' INTO TABLE \`$TABLE\` CHARACTER SET utf8 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES SET \`sem\` = 1, \`ano\` = $YEAR;"
			echo "Loading file $FILE_HALF_2"
			mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "LOAD DATA INFILE '$FILE_HALF_2' INTO TABLE \`$TABLE\` CHARACTER SET utf8 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES SET \`sem\` = 2, \`ano\` = $YEAR;"
		done

		# Inserindo os dados do ultimo ano (nesse caso tem que verificar se já tem os dados do semestre 1 do ano atual ou só o do semestre 2 do ano passado)
		if [[ "$LAST_YEAR_LOAD" -ne "$ACTUAL_YEAR" ]]
		then
			FILE_HALF_1="$DATA_DIR/BRBRASIL/brbrasil_1_semestre_$LAST_YEAR_LOAD/${TABLE}_1_Semestre_$LAST_YEAR_LOAD.csv"
			FILE_HALF_2="$DATA_DIR/BRBRASIL/brbrasil_2_semestre_$LAST_YEAR_LOAD/${TABLE}_2_Semestre_$LAST_YEAR_LOAD.csv"
			echo "Loading file $FILE_HALF_1"
			mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "LOAD DATA INFILE '$FILE_HALF_1' INTO TABLE \`$TABLE\` CHARACTER SET utf8 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES SET \`sem\` = 1, \`ano\` = $LAST_YEAR_LOAD;"
			echo "Loading file $FILE_HALF_2"
			mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "LOAD DATA INFILE '$FILE_HALF_2' INTO TABLE \`$TABLE\` CHARACTER SET utf8 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES SET \`sem\` = 2, \`ano\` = $LAST_YEAR_LOAD;"
		else
			FILE_HALF_1="$DATA_DIR/BRBRASIL/brbrasil_1_semestre_$YEAR/${TABLE}_1_Semestre_$LAST_YEAR_LOAD.csv"
			echo "Loading file $FILE_HALF_1"
			mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "LOAD DATA INFILE '$FILE_HALF_1' INTO TABLE \`$TABLE\` CHARACTER SET utf8 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES SET \`sem\` = 1, \`ano\` = $LAST_YEAR_LOAD;"			
		fi

	done
}

function main {
	if [[ ! "$DB_PASS" || ! "$DB_USER" ]]
	then
		echo -e "Usage:\n\t$0 <DB_USER> <DB_PASS> <DATA_DIR>\n\t$0 <DB_USER> <DB_PASS>"
		exit -1
	fi
	[[ ! "$DATA_DIR" ]] && DATA_DIR=/tmp

	prepare_enviroment
	prepare_db
	load_domain_data
	load_semiannual_data

	echo -e "\nFinish!"
}

main
exit 0