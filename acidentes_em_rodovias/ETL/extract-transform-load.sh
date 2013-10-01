#!/bin/bash

# $DATA_DIR = diretório onde estão ou serão baixados os arquivos *.zip e *.csv (Padrão é /tmp)
# 
# 1) Antes Defina as permissoes de seguranca para o MySQL:
#	sudo nano /etc/apparmor.d/usr.sbin.mysqld
#		Coloque depois de "/run/mysqld/mysqld.sock w," essas duas linhas:
#		$DATA_DIR/ r,
#		$DATA_DIR/** rw,
#	sudo /etc/init.d/apparmor restart
#	sudo service mysql restart
# 2) Crie uma base de dados no MySQL com o nome 'acidentes_rodovias' e coloque o collation dele como utf8_bin
# 3) Caso já tenha os arquivos BRBRASIL.zip, tabelaPessoa.zip, estadofisico.csv e causaacidente.csv baixados, comente as linhas que dão 'wget' neles e coloque os arquivos em $DATA_DIR
# 4) Execute o programa:
#	Uso: ./extract-transform-load.sh <BD_USER> <BD_PASS> <DATA_DIR>
#	Ex: ./extract-transform-load.sh root 123456 /tmp

# TODO: 
#	- Fazer um log
#	- Receber parametros para definir quais operacoes serao feitas (so extrair? so transformar? so carregar? tudo junto?)
#	- Verificar conexao com a internet caso queira baixar os arquivos

DB_USER=$1
DB_PASS=$2
DATA_DIR=$3

function prepare_enviroment {
	echo -e "\nDownloading data..."
	wget -P $DATA_DIR http://repositorio.dados.gov.br/transportes-transito/transito/BRBRASIL.zip
	wget -P $DATA_DIR https://dl.dropboxusercontent.com/u/18364240/estadofisico.csv
	wget -P $DATA_DIR http://repositorio.dados.gov.br/transportes-transito/transito/causaacidente.csv
	wget -P $DATA_DIR http://repositorio.dados.gov.br/transportes-transito/transito/tabelaPessoa.zip

	if [[ ! -f "$DATA_DIR/BRBRASIL.zip" || ! -f "$DATA_DIR/tabelaPessoa.zip" || ! -f "$DATA_DIR/estadofisico.csv" || ! -f "$DATA_DIR/causaacidente.csv" ]]
	then
		echo "ERROR: Files $DATA_DIR/BRBRASIL.zip, $DATA_DIR/tabelaPessoa.zip, $DATA_DIR/causaacidente.csv or $DATA_DIR/estadofisico.csv dont exist"
		exit -1
	fi

	echo -e "\nUnziping data..."
	unzip -o -d $DATA_DIR $DATA_DIR/BRBRASIL.zip
	for i in $(ls $DATA_DIR/BRBRASIL/*.zip)
	do 
		unzip -o -d $DATA_DIR/BRBRASIL $i
	done
	unzip -o -d $DATA_DIR $DATA_DIR/tabelaPessoa.zip

	cp -f $DATA_DIR/estadofisico.csv $DATA_DIR/BRBRASIL
	cp -f $DATA_DIR/tabelaPessoa.csv $DATA_DIR/BRBRASIL/pessoa.csv
	cp -f $DATA_DIR/causaacidente.csv $DATA_DIR/BRBRASIL
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
	 	sed -i 's/\"\s\+\"/\\N/g' $i
	 	sed -i 's/;\\ ;/;\\N;/g' $i
	done
	for i in $(ls $DATA_DIR/BRBRASIL/*.csv)
	do 
		sed -i 's/(null)/\\N/g' $i
	 	sed -i 's/;;/;\\N;/g' $i
	 	sed -i 's/;\s\+;/;\\N;/g' $i
	 	sed -i 's/\"\s\+\"/\\N/g' $i
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

function load_non_semiannual_data {
	for TABLE in corveiculo localbr estadofisico marcadeveiculo municipio ocorrenciaveiculo tipoAcidente tipoApreensao tipoAreaEspecial tipoComunicacao tipocrime tipodetencao tipodocumento tipoenvolvido tipolocalidade tipoobra tipopontomedico tipopontonotavel tiporeceptor tiposinalizacao tipounidadeoperacional tipoveiculo uf unidadeoperacional veiculo causaacidente pessoa
	do
		echo -e "\nLoading non-semiannual table \"$TABLE\" data..."
		FILE="$DATA_DIR/BRBRASIL/$TABLE.csv"
		QUERY="LOAD DATA INFILE '$FILE' IGNORE INTO TABLE \`$TABLE\` CHARACTER SET utf8 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES;"
		mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "$QUERY"
	done
}

function load_semiannual_data {
	i=0
	for HALF in $(ls -d /tmp/BRBRASIL/brbrasil* | grep -E -o "_(1|2)_" )
	do
		HALFS[$i]="${HALF:1:1}" 
		((i++))
	done
	i=0
	for YEAR in $(ls -d /tmp/BRBRASIL/brbrasil* | grep -E -o "[0-9]{4}")
	do
		YEARS[$i]="$YEAR"
		((i++))
	done

	for TABLE in ocorrencia ocorrenciaacidente ocorrenciaPessoa #pessoa 
	do
		echo -e "\nLoading semiannual table \"$TABLE\" data..."
		# ID_COLUMN="$(head -1 $DATA_DIR/BRBRASIL/brbrasil_${HALFS[0]}_semestre_${YEARS[0]}/${TABLE}_${HALFS[0]}_Semestre_${YEARS[0]}.csv | sed -e 's/;/\n/g' | head -1)"
		# OTHER_COLUMNS="$(head -1 $DATA_DIR/BRBRASIL/brbrasil_${HALFS[0]}_semestre_${YEARS[0]}/${TABLE}_${HALFS[0]}_Semestre_${YEARS[0]}.csv | sed -e 's/;/\n/g' | tail -n+2 | sed ':a;N;$!ba;s/\n/\`,\`/g')"

		for (( i=0; i < ${#YEARS[@]}; i++ ))
		do
			FILE="$DATA_DIR/BRBRASIL/brbrasil_${HALFS[$i]}_semestre_${YEARS[$i]}/${TABLE}_${HALFS[$i]}_Semestre_${YEARS[$i]}.csv"
			QUERY="LOAD DATA INFILE '$FILE' IGNORE INTO TABLE \`$TABLE\` CHARACTER SET utf8 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES SET \`sem\` = ${HALFS[$i]}, \`ano\` = ${YEARS[$i]};"
			echo "Loading ${HALFS[$i]}-${YEARS[$i]}"
			mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "$QUERY"
		done
	done
}

function main {
	if [[ ! "$DB_PASS" || ! "$DB_USER" ]]
	then
		echo -e "Usage:\n\t$0 <DB_USER> <DB_PASS> <DATA_DIR>\n\t$0 <DB_USER> <DB_PASS>"
		exit -1
	fi
	[[ ! "$DATA_DIR" ]] && DATA_DIR=/tmp

	#prepare_enviroment
	prepare_db
	load_non_semiannual_data
	load_semiannual_data

	echo -e "\nFinish!"
}

main
exit 0
