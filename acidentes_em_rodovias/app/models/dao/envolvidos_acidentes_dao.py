# -*- coding: utf-8 -*-
"""@package Envolvidos Acidentes DAO
Data Access Object (DAO) para causa de acidentes nas BRs.

Este modulo contem declação da classe que acessa os
dados no banco e os exporta para a controller
"""

from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from models.envolvidos_acidentes import *
from util.estatisticas_util import *

class EnvolvidosAcidentesDAO(GenericoDAO):
	def envolvidos_acidentes(self):
		""" Envolvidos em Acidentes 

			Efetua uma query buscando por envolvidos em geral
			@return lista de objetos para as respostas da query
		"""
		query = """SELECT `quantidade_envolvidos`, `quantidade_acidentes`, `ano`
				FROM `estatisticas_envolvido`;"""

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "EnvolvidosAcidente", "envolvidos_acidentes")

	def media_desvio_envolvidos(self):
		""" Media e desvio dos envolvidos em acidentes 

			Retorna duas tuplas contendo os desvios e media dos envolvidos.
			@return lista de objetos para as respostas da query
		"""
		lista_envolvidos = self.envolvidos_acidentes()

		lista_medias = []
		for envolvido in lista_envolvidos:
			envolvidos = float(envolvido.quantidade_envolvidos)
			acidentes = float(envolvido.quantidade_acidentes)
			media = envolvidos/acidentes
			lista_medias.append(media)

		desvio = desvio_padrao(lista_medias)

		return lista_medias, desvio

