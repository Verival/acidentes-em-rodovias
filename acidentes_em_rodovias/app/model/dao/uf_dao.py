# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
from model.uf import *

class UfDAO(GenericoDAO):
	def lista_ufs(self, limite=0):
		if(limite != 0):
			limite = 'LIMIT %s' % limite
		else:
			limite = ''

		query = """SELECT tufuf, tufdenominacao
			FROM uf ORDER BY tufdenominacao %s;""" % limite
		
		return self.transforma_dicionario_em_objetos(self.executa_query(query), "Uf", "uf")