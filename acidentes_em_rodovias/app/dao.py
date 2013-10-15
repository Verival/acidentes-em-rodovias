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
		
class MunicipioDAO(DAO):
	def __init__(self):
		DAO.__init__(self, "municipio")
	def consulta_por_uf(self, uf,limit=0):
		if(limit !=0):
			limit = "LIMIT " + str(limit)
		else:
			limit = ''
		query = "SELECT * FROM `%s` WHERE `tmuuf` = '%s'" % (self.modelo, uf)
		dados = psql.frame_query(query,con=self.connection).to_dict()
		 
		return util.transforma_para_objeto(dados, self.modelo)

class OcorrenciaDAO(DAO):
	def __init__(self):
		DAO.__init__(self, "ocorrencia")
	def consulta_por_uf(self, uf,limit=0):
		if(limit !=0):
			limit = "LIMIT " + str(limit)
		else:
			limit = ''
		ret=[]
		mun = MunicipioDAO()
		mun_id = [ i.tmucodigo for i in mun.consulta_por_uf(uf)]
		for _id in mun_id:
			query = "SELECT * FROM `%s` WHERE `ocomunicipio` = '%d'" % (self.modelo, _id)
			dados = psql.frame_query(query,con=self.connection).to_dict()
		 
			ret.append( util.transforma_para_objeto(dados, self.modelo))
		return ret

if __name__ == "__main__":
	#consulta municipios do Espirito Santo
	mun = MunicipioDAO()	
	for i in mun.consulta_por_uf('ES'):
		print i
	
	#consulta ocorrencias do Espirito Santo
	oco = OcorrenciaDAO()
	for i in oco.consulta_por_uf('ES',10):
		for j in i:
			if (j.ocomunicipio== 56839): # Filtra apenas os que aconteceram em PIUMA
				print j
	
