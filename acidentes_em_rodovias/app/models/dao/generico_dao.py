# -*- coding: utf-8 -*-
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


import myconfiguration
import MySQLdb
import pandas.io.sql as psql
from exception.internal_exceptions import *
#from uf_dao import *
import importlib
import logging
logging.basicConfig()


logger = logging.getLogger(__name__)
class GenericoDAO:
	def __init__(self):
		self.usuario = myconfiguration.DB_USER
		self.senha = myconfiguration.DB_PASS
		self.database = myconfiguration.DB
		self.host = myconfiguration.HOST		
		self.conexao = self.get_conexao()

	def get_conexao(self):
		conexao = MySQLdb.connect(self.host, self.usuario, self.senha, self.database)
		return conexao
	

	def executa_query(self, query, get_data_frame=False):
		dados = None
		
		if (get_data_frame is False):
			dados = psql.frame_query(query, con=self.conexao).to_dict()
		else:
			dados = psql.frame_query(query, con=self.conexao)

		if (dados is None):
			raise ResultadoConsultaNuloError("A biblioteca pandas não está instalada, ou nenhum dado foi passado a esse método")
		else:
			return dados

	def transforma_dicionario_em_objetos(self, dados, nome_classe, nome_modulo):
		modulo_classe = importlib.import_module("models." + nome_modulo)
		class_ = getattr(modulo_classe, nome_classe)
		lista_objetos = []

		try:
			chaves = dados.keys()
		except AttributeError, e:	# foi enviado uma lista nula para ser transformada
			raise ResultadoConsultaNuloError("A biblioteca pandas não está instalada, ou nenhum dado foi passado a esse método")
		
		for i in range(0, len(dados[chaves[0]])):
			instancia = class_()
			for chave in chaves:
				if (isinstance(dados[chave][i], basestring)):
					setattr(instancia, chave, dados[chave][i].decode('iso-8859-1').encode('utf8'))
				else:
					setattr(instancia, chave, dados[chave][i])
			lista_objetos.append(instancia)

		return lista_objetos
		


if __name__ == '__main__':
	import numpy as np
	dao=GenericoDAO()
	#for i in range(15):
	#	print str(2000+i)
	outras=[]
	dados={'ano':[],'Total':[]}
	for i in range(7):
		query="""SELECT ca.tcadescricao, COUNT( * ) AS  'quantidade_ocorrencias'
				FROM ocorrencia AS o
				INNER JOIN ocorrenciaacidente AS oa ON o.ocoid = oa.oacocoid
				INNER JOIN causaacidente AS ca ON oa.oactcacodigo = ca.tcacodigo
				WHERE o.ano =%s
				GROUP BY ca.tcadescricao
				ORDER BY COUNT( * ) DESC 
				LIMIT 0 , 30"""%(i+2007)
		q_ret=psql.frame_query(query, con=dao.conexao)
		print '-----------------ANO--%s------------------'%(2007+i)
		dados['ano'].append(2007+i)
		for (k,n) in zip(q_ret[q_ret.keys()[0]],range(11)):
		 	if k in dados :
		 		dados[k].append(q_ret.as_matrix()[n][1])
		 	else:
		 		dados[k]=[]
		 		dados[k].append(q_ret.as_matrix()[n][1])
		dados['Total'].append(q_ret.sum()['quantidade_ocorrencias'])
	
	print dados
	for i in dados:
		print "Média de %s: %f" %(i,np.mean(dados[i]))
		print "Total de %s: %f" %(i,np.sum(dados[i]))
	for (ano,total) in zip(dados['ano'],dados['Total']):
		print "Total no ano de %i: %i"%(ano,total)
'''
	print '------------------------------------------'
	print q_ret.describe().as_matrix()[1]
	print '------------------------------------------'
	print q_ret.as_matrix()
	print '------------------------------------------'
	#print q_ret.apply(Series.interpolate,axies=1)
'''
