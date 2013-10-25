# -*- coding: utf-8 -*-
import sys, os, inspect
current_path = os.path.abspath('..')
sys.path.append(current_path)

import MySQLdb

class DAO:
	def __init__(self, senha = '1234'):
		self.usuario = 'root'
		self.senha = senha
		self.database = 'acidentes_rodovias'
		self.host = 'localhost'

	def inicia_conexao(self):
		try:
			self.conexao = MySQLdb.connect(self.host, self.usuario, self.senha)
			self.conexao.select_db(self.database)
		except:
			self.conexao.rollback()

	def executa_query(self, query):
		try:
			cursor = self.conexao.cursor()
			cursor.execute(query)
		except:
			self.conexao.rollback()
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