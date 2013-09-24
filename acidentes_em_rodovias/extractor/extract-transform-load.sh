#!/bin/bash

# 1) Antes Defina as permissoes de seguranca para o MySQL:
#	sudo nano /etc/apparmor.d/usr.sbin.mysqld -> Coloque $DATA_DIR/ r, $DATA_DIR/** rw
#	sudo /etc/init.d/apparmor restart
#	sudo service mysql restart
# 2) Crie uma base de dados com o nome 'acidentes_rodovias' e coloque o collation dele como utf8_bin
# 3) Caso já tenha os arquivos BRBRASIL.zip e estadofisico.csv baixados, comente as linhas que dão 'wget' neles e coloque os arquivos em $DATA_DIR

# TODO: - Verificar retornos dos comandos MySQL (variavel $?) 
#		- Fazer um log
#		- Receber parametros para definir quais operacoes serao feitas
#		- Verificar conexao com a internet

DATA_DIR=/tmp
DB_USER=usuario
DB_PASS=senha

function prepare_enviroment {
	echo -e "\nDownloading data..."
	wget -P $DATA_DIR http://repositorio.dados.gov.br/transportes-transito/transito/BRBRASIL.zip
	wget -P $DATA_DIR https://dl.dropboxusercontent.com/u/18364240/estadofisico.csv

	echo -e "\nUnziping data..."
	unzip -o -d $DATA_DIR $DATA_DIR/BRBRASIL.zip
	for i in $(ls $DATA_DIR/BRBRASIL/*.zip); do 
		unzip -o -d $DATA_DIR/BRBRASIL $i
	done
	mv estadofisico.csv $DATA_DIR/BRBRASIL
	rm -f $DATA_DIR/BRBRASIL/*.zip $DATA_DIR/BRBRASIL/*.pdf

	echo -e "\nStandardizing delimiters..."
	sed -i 's/|/;/g' "$DATA_DIR/BRBRASIL/veiculo.csv"
	sed -i 's/|/;/g' "$DATA_DIR/BRBRASIL/ocorrenciaveiculo.csv"

	echo -e "\nStandardizing null cells to \N..."
	for i in $(ls $DATA_DIR/BRBRASIL/**/*.csv); do 
	 	sed -i 's/(null)/\\N/g' $i
		sed -i 's/;;/;\\N;/g' $i
	 	sed -i 's/;\s\+;/;\\N;/g' $i
	 	sed -i 's/;\\ ;/;\\N;/g' $i
	done
	for i in $(ls $DATA_DIR/BRBRASIL/*.csv); do 
		sed -i 's/(null)/\\N/g' $i
	 	sed -i 's/;;/;\\N;/g' $i
	 	sed -i 's/;\s\+;/;\\N;/g' $i
		sed -i 's/;\\ ;/;\\N;/g' $i
	done	
}

function prepare_db {
	echo -e "\nLoading database schema..."
	mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias < $(dirname $0)/esquema-banco.sql
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
		if [ "$LAST_YEAR_LOAD" -ne "$ACTUAL_YEAR" ]
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

# MAIN
prepare_enviroment
prepare_db
load_semiannual_data
load_domain_data

echo -e "\nFinish!"

exit 0