# -*- coding: utf-8 -*- 

#Codigo de Exemplo para uso do MySQLdb

import warnings
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
		warnings.warn("Deprecated", DeprecationWarning)
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
	
		#coletando warnings	
		with warnings.catch_warnings(record=True) as w:
			print "Utilizando método não recomendado."
			t=raw_input("PRESS ENTER TO CONTINUE.\n")
		
class MunicipioDAO(DAO):
	def __init__(self):
		DAO.__init__(self, "municipio")
	def consulta_por_uf(self, uf,limit=0):
		if(limit !=0):
			limit = "LIMIT " + str(limit)
		else:
			limit = ''
		query = "SELECT * FROM `%s` WHERE `tmuuf` = '%s' %s" % (self.modelo, uf,limit)
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
			query = "SELECT * FROM `%s` WHERE `ocomunicipio` = '%d' %s" % (self.modelo, _id,limit)
			dados = psql.frame_query(query,con=self.connection).to_dict()
		 
			ret.append( util.transforma_para_objeto(dados, self.modelo))
		return ret

class OcorrenciaResultadosDAO():
	def __init__(self):
		self.modelo = "OcorrenciaResultados"
		self.connection = util.get_connection()
		
	def consulta_por_municipio(self, municipio_id, limit=0):
		if(limit !=0):
			limit = "LIMIT " + str(limit)
		else:
			limit = ''
		query = """
		SELECT oco.ocoid,
		oco.ocodataocorrencia, 
		oco.ocodataregistro, 
		mun.tmuuf, 
		mun.tmudenominacao, 
		uo.unidenominacao, 
		uo.uniendereco, 
		tuo.ttudescricao, 
		mvei.tmvdescricao, 
		tco.tcodescricao

		FROM ocorrencia oco, 
		municipio mun, 
		unidadeoperacional uo, 
		tipounidadeoperacional tuo, 
		ocorrenciaveiculo ocov,
		veiculo vei,
		marcadeveiculo mvei,
		tipoComunicacao tco

		WHERE oco.ocomunicipio = mun.tmucodigo
		AND mun.tmucodigo = %d
		AND oco.ocotipo = tco.tcocodigo
		AND uo.unimunicipio = mun.tmucodigo  
		AND uo.unittucodigo = tuo.ttucodigo 
		AND ocov.ocvocoid = oco.ocoid 
		AND vei.veiid = ocov.ocvveiid
		AND mvei.tmvcodigo = vei.veitmvcodigo 

		%s
		""" % (municipio_id, limit)
		
		dados = psql.frame_query(query,con=self.connection).to_dict()

		return util.transforma_para_objeto(dados, self.modelo)

if __name__ == "__main__":
	dao = OcorrenciaResultadosDAO()
	dados = dao.consulta_por_municipio(132, 100)
	for i in dados:
		print i
	# #consulta municípios do Espirito Santo
	# mun = MunicipioDAO()	
	# for i in mun.consulta_por_uf('ES',5):
	# 	print i
	
	# #testa método depreciado
	# mun.troca_tabela("ocorrencia")
	
	# #consulta ocorrências do Espirito Santo
	# oco = OcorrenciaDAO()
	# for ocorrencias_es in oco.consulta_por_uf('ES',3): # Consulta de no máximo 10 por município
	# 	for j in ocorrencias_es: # Nas ocorrências do Espirito Santo
	# 		if (j.ocomunicipio== 56839): # Filtra apenas os que aconteceram em PIUMA
	# 			print j
	
