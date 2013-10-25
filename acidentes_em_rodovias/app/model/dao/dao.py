# -*- coding: utf-8 -*-
import sys, os, inspect
current_path = os.path.abspath('..')
sys.path.append(current_path)

import MySQLdb

class DAO:
	def __init__(self, senha='12345'):
		self.usuario = 'root'
		self.senha = senha
		self.database = 'acidentes_rodovias'
		self.host = 'localhost'
		self.conexao = None
	def inicia_conexao(self):
		try:
			self.conexao = MySQLdb.connect(self.host, self.usuario, self.senha)
			self.conexao.select_db(self.database)
		except:
			if(self.conexao):
				self.conexao.rollback()
			print "Falha de conexão"

	def executa_query(self, query):
		try:
			cursor = self.conexao.cursor()
			cursor.execute(query)
		except:
			if(self.conexao):
				self.conexao.rollback()
			print "Falha na query"
		else:
			return cursor.fetchall()

#TODO: Passar pro teste!!!
if __name__ == '__main__':
	if(len(sys.argv)>1):
		dao = DAO(sys.argv[1])
	else:
		dao = DAO()

	dao.inicia_conexao()
	print dao.executa_query('show * tables')
