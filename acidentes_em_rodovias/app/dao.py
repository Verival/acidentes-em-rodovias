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
		#estabilizando estrutura
		self.modelo=modelo.lower()
		self.modelo = self.modelo[0].upper() +  self.modelo[1:]
		self.connection = util.get_connection()
		print self.modelo
	
	def consulta_todos(self):
		dados = psql.frame_query("SELECT * FROM " +self.modelo.lower()+" LIMIT 10;",con=self.connection).to_dict()
		classe = self.modelo
		return util.transforma_para_objeto(dados, classe)


if __name__ == "__main__":
	dao = DAO('Ocorrencia')

	for i in dao.consulta_todos():
		print i
