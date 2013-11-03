Instalação Sonar + pyLint + Sonar-Runner + Python Plugin + Coverage
========================================================

Passos para instalação do ambiente de coleta de métricas.

### Instalação do Sonar
* Instalar Sonar ou utilizar o deb
* gksudo gedit /etc/apt/sources.list
* Inserir a linha: deb http://downloads.sourceforge.net/project/sonar-pkg/deb binary/
* sudo apt-get update
* sudo apt-get install sonar
* Sonar instalado em /opt/sonar

### Instalação do Sonar Runner
* Baixe: http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-dist/2.3/sonar-runner-dist-2.3.zip
* Descompacte em /opt/: sudo unzip sonar-runner-dist-2.3.zip /opt/

### Instalando Outros
* sudo apt-get install pylint
* Caso não tenha pip: sudo apt-get install python-pip 
* sudo pip install coverage
* Caso não tenha django: sudo pip install django

### Configuração do Sonar 
* Abra o arquivo /opt/sonar/conf/sonar.properties: sudo gedit /opt/sonar/conf/sonar.properties
* Comente para linha: 

```
# Comment the following line to deactivate the default embedded database.
                     #sonar.jdbc.url:                            jdbc:h2:tcp://localhost:9092/sonar
```
* Descomente para linha: 

```
# Comment the embedded database and uncomment the following line to use MySQL
                        sonar.jdbc.url:                            jdbc:mysql://localhost:3306/sonar?useUnicode=true&characterEncoding=utf8&rewriteBatchedStatements=true
```
* Caso esteja comentado, descomente #---- Credentials e garanta que username e password estejam sonar
* Salve o arquivo

### Configuração do Sonar-Runner
* Abra o arquivo /opt/sonar-runner-2.3/conf/sonar-runner.properties: sudo gedit /opt/sonar-runner.properties/conf/sonar-runner.properties
* Descomente a linha do MySql
* Descomente a linha do Default SonarQube server.... sonar.host.url
* Salve o arquivo:


### Configuração do projeto
* Abra a pasta do projeto django(Aonde se encontra o manage.py)
* Crie o arquivo sonar-project.properties: sudo touch sonar-project.properties
* Insira o seguinte:

```
sonar.projectKey=gppmds:acidentes-rodovias
sonar.projectName=Acidentes em Rodovias
sonar.projectVersion=1.0

sonar.projectDescription=Projeto de GPP/MDS

sonar.sources=app

sonar.language=py

sonar.sourceEncoding=UTF-8

sonar.python.coverage.reportPath=app/tests/test-reports/coverage.xml
```

* Salve o arquivo
* Crie a pasta /app/tests/test-reports

### Configurando banco
* Execute o comando mysql:
* Command: mysql -u root -p mysql
* Execute o comando:

``` 
CREATE DATABASE sonar CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER 'sonar' IDENTIFIED BY 'sonar';
GRANT ALL ON sonar.* TO 'sonar'@'%' IDENTIFIED BY 'sonar';
GRANT ALL ON sonar.* TO 'sonar'@'localhost' IDENTIFIED BY 'sonar';
FLUSH PRIVILEGES;
```

* execute exit() para fechar

### Iniciando serviços e projetos
* Execute o comando sonar.sh start: sudo /opt/sonar/bin/sonar.sh start
* Entre em http://localhost:9000
* Login(superior direito): admin, admin
* Settings->Update Center->Available Plugins: Python-> Install
* Cancele o servidor sonar ou: sudo /opt/sonar/bin/sonar.sh restart
* Vá para pasta do projeto e execute sonar-runner: sudo /opt/sonar-runner-2.3/bin/sonar-runner

### Testes unitarios
* Execute: sudo coverage erase
* Execute na pasta do projeto: sudo coverage run --source='.' manage.py test app
* Execute: sudo coverage xml -i -o app/tests/test-reports/coverage.xml
* Execute: sudo /opt/sonar-runner-2.3/bin/sonar-runner

