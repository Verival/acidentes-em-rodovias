# -*- coding: utf-8 -*-
"""@package Municipios
Declaração das classes para tipos de acidentes.

Este modulo contem declação da classe de modelo
para tipos de acidentes
"""

class TiposAcidentes:
	""" Tipos de acidentes """
	def __init__(self):
		self.tipo = ''
		self.quantidade_ocorrencias = 0

class TiposAcidentesAno:
	""" Tipos de acidentes por ano"""
	def __init__(self):
		self.tipo = ''
		self.quantidade_ocorrencias_list = []
		self.ano_list = []

class ProbabilidadeTiposAcidentes:
	""" Probabilidade de tipos de acidentes """
	def __init__(self):
		self.tipo = ''
		self.probabilidade_por_limite_list = []	

class MediaDesvioTiposAcidentes:
	""" Media e desvio padrão de tipos de acidentes """
	def __init__(self):
		self.tipo = ''
		self.media = 0.0
		self.desvio = 0.0