# -*- coding: utf-8 -*- 

#Codigo de Exemplo para uso do MySQLdb

import util
import pandas.io.sql as psql

class DAO():
	modelo=''
	keys=[]
	def __init__(self,modelo):
		try:
			self.connection = util.get_connection()

			self.modelo=modelo.lower()
			dados = psql.frame_query("SHOW TABLES;",con=self.connection).to_dict('list')
			self.keys = dados['Tables_in_acidentes_rodovias']
			minimos = [i.lower() for i in self.keys]
			if self.modelo in minimos:
				self.modelo = self.keys[minimos.index(self.modelo)]
			else:
				self.modelo=''
				raise Exception("Tabela " + modelo + " não existente")
		except Exception, ex:
			print ex
			print "Existentes:\n " + str(self.keys)
			
	def troca_tabela(self, modelo):
		try:
			minimos = [i.lower() for i in self.keys]
			if modelo in minimos:
				self.modelo = self.keys[minimos.index(modelo)]
			else:
				self.modelo=''
				raise Exception("Tabela " + modelo + " não existente")
		except Exception, ex:
			print ex
			print "Existentes:\n " + str(self.keys)
			
	
	def consulta_todos(self,limit=0):
		if(self.modelo != ''):
			if(limit !=0):
				limit = "LIMIT " + str(limit)
			else:
				limit = ''
			query = "SELECT * FROM %s %s" %(self.modelo,limit)
			dados = psql.frame_query(query,con=self.connection).to_dict()
			return util.transforma_para_objeto(dados, self.modelo)
		return []

if __name__ == "__main__":
	#exemplo de teste
	dao = DAO('ocorrencia')
	for i in dao.consulta_todos(3):
		print i
	dao.troca_tabela("essoa")
	for i in dao.consulta_todos(3):
		print i

