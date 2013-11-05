# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
#from model.uf import *

class UfDAO(GenericoDAO):
	def lista_ufs(self, limite=0):
		if(limite != 0):
			limite = 'LIMIT %s' % limite
		else:
			limite = ''
		try:
			query = """SELECT tufuf, tufdenominacao
				FROM uf ORDER BY tufdenominacao %s;""" % limite
		except OperationError as e:
			sys.stderr.write("Falha na comunicação: " + str(e))
			return None
		except InternalError as e:
			sys.stderr.write("Erro de sincronia: " + str(e))
			return None
		except NotSuportedError as e:
			sys.stderr.write("Operação não suportada: " + str(e))
			return None

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "Uf", "uf")