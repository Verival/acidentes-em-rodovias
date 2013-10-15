# -*- coding: utf-8 -*- 
import MySQLdb
import myconfiguration
import models

def get_connection():
	try:
		connection = MySQLdb.connect(myconfiguration.HOST, myconfiguration.DB_USER, 
			myconfiguration.DB_PASS, myconfiguration.DB)	# Aqui inicia a conexão com o Banco.
		if connection:
			return connection
		else:
			raise Exception("Erro na conexão com o Banco de Dados")
	except Exception, ex:
		print ex


def transforma_para_objeto(dados, nome_classe):
	class_ = getattr(models, nome_classe)
	lista_objetos = []
	
	chaves = dados.keys()
	
	for i in range(0, len(dados[chaves[0]])):
		instancia = class_()
		for chave in chaves:
			setattr(instancia, chave, dados[chave][i])
		lista_objetos.append(instancia)

	return lista_objetos