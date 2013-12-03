# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO

class MunicipioDAO(GenericoDAO):
	def lista_municipios(self, uf, limite=0):
		if(limite != 0):
			limite = 'LIMIT %s' % limite
		else:
			limite = ''

		query = """SELECT DISTINCT tmucodigo, tmudenominacao, tmuuf
				FROM municipio tmu
				INNER JOIN ocorrencia oco ON oco.ocomunicipio = tmu.tmucodigo
		 		WHERE tmu.tmuuf = '%s' ORDER BY tmudenominacao %s; """ % (uf, limite)
			
		return self.transforma_dicionario_em_objetos(self.executa_query(query), "Municipio", "municipio")