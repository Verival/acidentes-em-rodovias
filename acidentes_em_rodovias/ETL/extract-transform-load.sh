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
# 2) Crie uma base de dados no MySQL com o nome 'acidentes_rodovias' e coloque o collation dele como latin1_general_ci
# 3) Caso já tenha os arquivos *.zip baixados, comente a linha que da 'wget' neles e coloque os arquivos em $DATA_DIR/acidentes_rodovias/zips (crie as pastas caso elas não existam)
# 4) Execute o programa:
#	Uso: ./extract-transform-load.sh <BD_USER> <BD_PASS> <DATA_DIR>
#	Exemplo: ./extract-transform-load.sh root 123456 /tmp

DB_USER=$1
DB_PASS=$2
DATA_DIR=$3

function prepare_enviroment {
	echo -e "\nDownloading data..."
	mkdir -p $WORK_DIR/zips
	wget -P $WORK_DIR/zips/ -r --no-parent -l 1 --accept="*.zip" --no-directories  http://repositorio.dados.gov.br/transportes-transito/transito/

	if [[ ! -f "$WORK_DIR/zips/dominios.zip" || ! -f "$WORK_DIR/zips/brbrasil_1_semestre_2008.zip" || ! -f "$WORK_DIR/zips/pessoas_e_veiculos.zip" ]]
	then
		echo "ERROR: Files $DATA_DIR/zips/dominio.zip, $DATA_DIR/zips/brbrasil*.zip or $DATA_DIR/zips/pessoas_e_veiculos.zip dont exist"
		exit -1
	fi

	echo -e "\nUnziping data..."
	unzip -o -d $WORK_DIR $WORK_DIR/zips/\*.zip
	mv $WORK_DIR/tabelaPessoa.csv $WORK_DIR/pessoa.csv

	echo -e "\nStandardizing delimiters..."
	sed -i 's/|/;/g' "$WORK_DIR/ocorrenciaveiculo.csv"

	echo -e "\nStandardizing null cells to \N..."
	for i in $(ls $WORK_DIR/**/*.csv)
	do 
	 	sed -i 's/(null)/\\N/g' $i
		sed -i 's/;;/;\\N;/g' $i
	 	sed -i 's/;\s\+;/;\\N;/g' $i
	 	sed -i 's/\"\s\+\"/\\N/g' $i
	 	sed -i 's/;\\ ;/;\\N;/g' $i
	done
	for i in $(ls $WORK_DIR/*.csv)
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

function load_non_biannual_data {
	for TABLE in ocorrenciaveiculo veiculo pessoa
	do
		echo -e "\nLoading non-biannual table \"$TABLE\" data..."
		FILE="$WORK_DIR/$TABLE.csv"
		QUERY="LOAD DATA INFILE '$FILE' IGNORE INTO TABLE \`$TABLE\` CHARACTER SET latin1 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES;"
		mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "$QUERY"
	done
}

function load_domain_data {
	for TABLE in corveiculo localbr estadofisico marcadeveiculo municipio tipoAcidente tipoApreensao tipoAreaEspecial tipoComunicacao tipocrime tipodetencao tipodocumento tipoenvolvido tipolocalidade tipoobra tipopontomedico tipopontonotavel tiporeceptor tiposinalizacao tipounidadeoperacional tipoveiculo uf unidadeoperacional causaacidente paises pnv
	do
		echo -e "\nLoading domain table \"$TABLE\" data..."
		FILE="$WORK_DIR/$TABLE.csv"
		QUERY="LOAD DATA INFILE '$FILE' IGNORE INTO TABLE \`$TABLE\` CHARACTER SET latin1 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES;"
		mysql -u $DB_USER --password=$DB_PASS acidentes_rodovias -e "$QUERY"
	done
}

function load_biannual_data {
	i=0
	for HALF in $(ls -d $WORK_DIR/brbrasil* | grep -E -o "_(1|2)_" )
	do
		HALFS[$i]="${HALF:1:1}" 
		((i++))
	done
	i=0
	for YEAR in $(ls -d $WORK_DIR/brbrasil* | grep -E -o "[0-9]{4}")
	do
		YEARS[$i]="$YEAR"
		((i++))
	done

	for TABLE in ocorrencia ocorrenciaacidente ocorrenciaPessoa
	do
		echo -e "\nLoading biannual table \"$TABLE\" data..."

		for (( i=0; i < ${#YEARS[@]}; i++ ))
		do
			FILE="$WORK_DIR/brbrasil_${HALFS[$i]}_semestre_${YEARS[$i]}/${TABLE}_${HALFS[$i]}_Semestre_${YEARS[$i]}.csv"
			QUERY="LOAD DATA INFILE '$FILE' IGNORE INTO TABLE \`$TABLE\` CHARACTER SET latin1 FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES SET \`sem\` = ${HALFS[$i]}, \`ano\` = ${YEARS[$i]};"
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
	
	WORK_DIR="$DATA_DIR/acidentes_rodovias"

	prepare_enviroment
	prepare_db
	load_domain_data
	load_non_biannual_data
	load_biannual_data

	echo -e "\nFinish!"
}

main
exit 0
