# -*- coding: utf-8 -*- 

#Codigo de Exemplo para uso do MySQLdb

import util
import pandas.io.sql as psql

# connection = MySQLdb.connect('localhost', 'root', '1234')	# Aqui inicia a conexão com o Banco.
# 															# Os parametros são: servidor, usuario e senha.

# connection.select_db('test')	# Seleciona o Banco de Dados.

# query = connection.cursor()	# Cursor que será usado para executar as queries.

# query.execute('SELECT * FROM test_table')	# Query que será executada, no caso, um SLECT simples.

# # Agora vem a parte magica :)

# result = query.fetchone()	# Pega só uma linha. Se voce continuar usando o 'fetchone()', ele vai pegando a proxima linha.

# print 'Pega uma linha: ', result


# query.execute('SELECT * FROM test_table')
# result = query.fetchall()	# Pega todas as linhas

# print '\nPega todas as linhas: ', result

class DAO():
	modelo=''
	def __init__(self,modelo):
		self.connection = util.get_connection()

		self.modelo=modelo.lower()
		dados = psql.frame_query("SHOW TABLES;",con=self.connection).to_dict('list')
		dados = dados['Tables_in_acidentes_rodovias']
		minimos = [i.lower() for i in dados]
		if self.modelo in minimos:
			self.modelo = dados[minimos.index(self.modelo)]
	
	def consulta_todos(self):
		dados = psql.frame_query("SELECT * FROM " +self.modelo+" LIMIT 10;",con=self.connection).to_dict()
		classe = self.modelo
		return util.transforma_para_objeto(dados, classe)

if __name__ == "__main__":
	#exemplo de teste
	dao = DAO('ocorrencia')
	for i in dao.consulta_todos():
		print i

