# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

class UFAcidentesDAO(GenericoDAO):
	def acidentes_uf_geral(self):
		query = """SELECT ufe.uf, SUM(ufe.quantidade_ocorrencias) AS quantidade_ocorrencias
				FROM estatisticas_uf ufe
				GROUP BY ufe.uf
				ORDER BY quantidade_ocorrencias DESC;"""

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "UFAcidentes", "uf_acidentes")
