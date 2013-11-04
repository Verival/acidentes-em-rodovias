#! /bin/bash
DB_USER=$1
DB_PASS=$2

if [[ ! "$DB_PASS" && "$DB_USER" ]]
  then
    DB_PASS=$DB_USER
    DB_USER=root
  fi
if [[ ! "$DB_PASS" || ! "$DB_USER" ]]
	then
		echo -e "Usage:\n\t$0 <DB_USER> <DB_PASS> \n\t$0 <DB_PASS>"
		exit -1
	fi
	
	apt-get install python-pip
	pip install coverage
	pip install pylint
	
	echo Usando User: $DB_USER e PASS: $DB_PASS
	#sonar-runner
	DIRECTORY=/opt/sonar-runner-2.3
	if [ ! -d "$DIRECTORY" ]; then
	  wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-dist/2.3/sonar-runner-dist-2.3.zip
	  unzip sonar-runner-dist-2.3.zip -d /opt/
	  rm sonar-runner-dist-2.3.zip
  fi
  #sonar
  DIRECTORY=/opt/sonar
  if [ ! -d "$DIRECTORY" ]; then
    wget http://dist.sonar.codehaus.org/sonar-3.7.3.zip
    unzip sonar-3.7.3.zip -d /opt
    rm sonar-3.7.2.zip
	fi
	
	#sonar database
  QUERY="CREATE DATABASE sonar CHARACTER SET utf8 COLLATE utf8_general_ci;CREATE USER 'sonar' IDENTIFIED BY 'sonar';GRANT ALL ON sonar.* TO 'sonar'@'%' IDENTIFIED BY 'sonar';GRANT ALL ON sonar.* TO 'sonar'@'localhost' IDENTIFIED BY 'sonar';FLUSH PRIVILEGES;"
  mysql -u $DB_USER --password=$DB_PASS mysql -e "$QUERY"
  
  sed -i "48s/.*/#/" /opt/sonar/conf/sonar.properties
  sed -i "58s/.*/sonar.jdbc.url:                            jdbc:mysql:\/\/localhost:3306\/sonar?useUnicode=true\&characterEncoding=utf8\&rewriteBatchedStatements=true/" /opt/sonar/conf/sonar.properties

  sed -i "5s/.*/sonar.host.url=http:\/\/localhost:9000/" /opt/sonar-runner-2.3/conf/sonar-runner.properties
  sed -i "11s/.*/sonar.jdbc.url=jdbc:mysql:\/\/localhost:3306\/sonar?useUnicode=true\&amp;characterEncoding=utf8/" /opt/sonar-runner-2.3/conf/sonar-runner.properties

  /opt/sonar/bin/linux-x86-64/sonar.sh start&
  
  
  pylint --generate-rcfile > ~/.pylintrc
  sed -i "8s/.*/init-hook=import sys; sys.path.insert(0, 'app');/" ~/.pylintrc  
  
  echo "------------------------------------------------------------------------"
  echo "Esperando primeira configuração do sonar(lenta)"
  echo "No meu demorou 3 minutos, entao sleep por 3min e 30s por segurança"
  echo "------------------------------------------------------------------------"
  sleep 2
  echo "Pode checar usando: tailf /opt/sonar/logs/sonar.log"
  echo ""
  sleep 1
  echo "Quando parar aparacer logs, sonar configurado... "
  echo ""
  sleep 1
  echo "Acesse http://localhost:9000"
  echo ""
  sleep 1
  echo "Log in com admin admin(superior esquedo da tela)"
  echo ""
  sleep 1
  echo "Settings->Update Center->Available Plugins->Pythons ... Install"
  echo ""
  sleep 1
  echo "Resete o servido com: /opt/sonar/bin/linux-x86-64/sonar.sh restart&"
  echo ""
  echo "Para ativar metricas pylint. No sonar: Quality Profiles->Python Profiles->Create"
  sleep 1
  echo "Em search: Repository->Pylint, Activation->Any, Search"
  sleep 1
  echo "Bulk Change(esquerda): Activate all. (demora alguns segundos)"
  sleep 1
  echo "Volte e setDefault o profile criado."
  sleep 4
  echo "FINALMENTE: rode o script ./server_coverage.sh"
  echo ""
  sleep 1
  echo "--- CONGRATZ, se tudo der certo, o projeto aparecerá em localhost:9000"
  echo ""




