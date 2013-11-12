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
		if (get_data_frame == False):
			return psql.frame_query(query, con=self.conexao).to_dict()
		else:
			return psql.frame_query(query, con=self.conexao)

	def transforma_dicionario_em_objetos(self, dados, nome_classe, nome_modulo):
		modulo_classe = importlib.import_module("models." + nome_modulo)
		class_ = getattr(modulo_classe, nome_classe)
		lista_objetos = []

		try:
			chaves = dados.keys()
		except AttributeError, e:	# foi enviado uma lista nula para ser transformada
			raise NoPandasComponentError("A biblioteca pandas não está instalada ou está desatualizada")
		
		for i in range(0, len(dados[chaves[0]])):
			instancia = class_()
			for chave in chaves:
				if (isinstance(dados[chave][i], basestring)):
					setattr(instancia, chave, dados[chave][i].decode('iso-8859-1').encode('utf8'))
				else:
					setattr(instancia, chave, dados[chave][i])
			lista_objetos.append(instancia)

		return lista_objetos
		
