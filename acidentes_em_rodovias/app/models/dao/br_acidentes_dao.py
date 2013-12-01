# -*- coding: utf-8 -*-
"""@package BR Acidentes DAO
Data Access Object (DAO) para acidentes nas BRs.

Este modulo contem declação da classe que acessa os
dados no banco e  os exporta para a controller
"""

from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from models.br_acidentes import *

class BRAcidentesDAO(GenericoDAO):
	""" BR Acidentes DAO """
	def acidentes_br_geral(self):
		""" Acidentes em geral

			Efetua uma query buscando por acidentes em geral
			@return lista de objetos para as respostas da query
		"""
		query = """SELECT bre.br, SUM(bre.quantidade_ocorrencias) AS quantidade_ocorrencias
				FROM estatisticas_br bre
				GROUP BY bre.br
				ORDER BY bre.quantidade_ocorrencias DESC
				LIMIT 10;"""
		return self.transforma_dicionario_em_objetos(self.executa_query(query), 'BRAcidentes', 'br_acidentes')

	def acidentes_br_ano(self):
	""" Acidentes por ano

		Efetua uma query buscando por acidentes oorganizadas por ano
		@return lista de objetos para as respostas da query
	"""
		
		query = """SELECT bre.br, bre.quantidade_ocorrencias, bre.ano
				FROM estatisticas_br bre
				GROUP BY bre.ano, bre.br
				ORDER BY bre.br, bre.ano;"""
		
		resultado_query = self.executa_query(query)

		br_acidentes_ano_list = []
		ultima_br = ''
		for (br, quantidade_ocorrencias, ano) in zip(resultado_query['br'].values(), resultado_query['quantidade_ocorrencias'].values(), resultado_query['ano'].values()):
			br = br.decode('iso-8859-1').encode('utf8')
			if (ultima_br != br):
				brs_acidentes_ano =  BRAcidentesAno()
				br_acidentes_ano_list.append(brs_acidentes_ano)
				brs_acidentes_ano.br = br
				ultima_br = br
			brs_acidentes_ano.ano_list.append(ano)
			brs_acidentes_ano.quantidade_ocorrencias_list.append(quantidade_ocorrencias)

		return br_acidentes_ano_list