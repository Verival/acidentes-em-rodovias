# -*- coding: utf-8 -*-
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)


import myconfiguration
import MySQLdb
import pandas.io.sql as psql
#from uf_dao import *
import importlib

class GenericoDAO:
	def __init__(self):
		self.usuario = myconfiguration.DB_USER
		self.senha = myconfiguration.DB_PASS
		self.database = myconfiguration.DB
		self.host = myconfiguration.HOST
		self.conexao = self.get_conexao()

	def get_conexao(self):
		try:
			conexao = MySQLdb.connect(self.host, self.usuario, self.senha, self.database)
			return conexao
		except:
			print "Falha de conexão"

	def executa_query(self, query):
		try:
			return psql.frame_query(query, con=self.conexao).to_dict()
		except:
			print "Falha na query"

	def transforma_dicionario_em_objetos(self, dados, nome_classe, nome_modulo):
		modulo_classe = importlib.import_module("models." + nome_modulo)
		class_ = getattr(modulo_classe, nome_classe)
		lista_objetos = []

		chaves = dados.keys()
		
		for i in range(0, len(dados[chaves[0]])):
			instancia = class_()
			for chave in chaves:
				if (isinstance(dados[chave][i], basestring)):
					setattr(instancia, chave, dados[chave][i].decode('iso-8859-1').encode('utf8'))
				else:
					setattr(instancia, chave, dados[chave][i])
			lista_objetos.append(instancia)

		return lista_objetos

	def transforma_formato_da_data(self, data):
		dia = data[3:5]
		mes = data[:2]
		ano = data[6:]

		return ano + '-' + mes + '-' + dia

if __name__ == "__main__":
	dao = UfDAO()
	for i in dao.lista_ufs():
		print i.tufdenominacao