# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from datetime import datetime

class BRAcidentesDAO(GenericoDAO):
	def acidentes_br_geral(self):
		query = """SELECT bre.br, SUM(bre.quantidade_ocorrencias) AS quantidade_ocorrencias
				FROM estatisticas_br bre
				GROUP BY bre.br
				ORDER BY bre.quantidade_ocorrencias DESC
				LIMIT 10;"""
		return self.transforma_dicionario_em_objetos(self.executa_query(query), 'BRAcidentes', 'br_acidentes')

	def acidentes_br_ano(self):
		data = datetime.now()
		acidentes_br = []
		for ano in range(2007, data.year+1):
			query = """SELECT bre.br, bre.quantidade_ocorrencias, bre.ano
					FROM estatisticas_br bre
					WHERE bre.ano = '%s'
					GROUP BY bre.ano, bre.br
					ORDER BY bre.quantidade_ocorrencias DESC;""" % ano
			acidentes_ano = self.transforma_dicionario_em_objetos(self.executa_query(query), 'BRAcidentesAno', 'br_acidentes')
			acidentes_br.append(acidentes_ano)
		return acidentes_br
