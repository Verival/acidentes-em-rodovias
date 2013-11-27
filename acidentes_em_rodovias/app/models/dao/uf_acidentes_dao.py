# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from models.uf_acidentes import *

class UFAcidentesDAO(GenericoDAO):
	def acidentes_uf_geral(self):
		query = """SELECT ufe.uf, SUM(ufe.quantidade_ocorrencias) AS quantidade_ocorrencias
				FROM estatisticas_uf ufe
				GROUP BY ufe.uf
				ORDER BY quantidade_ocorrencias DESC;"""

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "UFAcidentes", "uf_acidentes")

	def acidentes_uf_ano(self):
		query = """SELECT u.tufdenominacao AS uf, ufe.quantidade_ocorrencias, ufe.ano
				FROM estatisticas_uf ufe
				INNER JOIN uf u
					ON u.tufuf = ufe.uf
				GROUP BY ufe.uf, ufe.ano
				ORDER BY ufe.uf;"""

		resultado_query = self.executa_query(query)

		uf_acidentes_ano_list = []
		ultima_uf = ''
		for (uf, quantidade_ocorrencias, ano) in zip(resultado_query['uf'].values(), resultado_query['quantidade_ocorrencias'].values(), resultado_query['ano'].values()):
			uf = uf.decode('iso-8859-1').encode('utf8')
			if (uf == '230' or uf == '470'):
				pass
			else:
				if (ultima_uf != uf):
					ufs_acidentes_ano =  UFAcidentesAno()
					uf_acidentes_ano_list.append(ufs_acidentes_ano)
					ufs_acidentes_ano.uf = uf
					ultima_uf = uf
				ufs_acidentes_ano.ano_list.append(ano)
				ufs_acidentes_ano.quantidade_ocorrencias_list.append(quantidade_ocorrencias)

		return uf_acidentes_ano_list