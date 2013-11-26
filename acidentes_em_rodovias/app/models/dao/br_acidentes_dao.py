# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

class BRAcidentesDAO(GenericoDAO):
	def acidentes_br_geral(self):
		query = """SELECT bre.br, bre.quantidade_ocorrencias
				FROM estatisticas_br bre
				GROUP BY bre.br
				ORDER BY bre.quantidade_ocorrencias DESC
				LIMIT 10;"""

		return self.transforma_dicionario_em_objetos(self.executa_query(query), 'BRAcidentes', 'br_acidentes')
