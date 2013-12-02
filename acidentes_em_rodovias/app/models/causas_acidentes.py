# -*- coding: utf-8 -*-
"""@package Modelo de acidentes
Declaração das classes para causas ou tipos de acidentes.

Este modulo contem declação das classes de modelo
para acidentes contendo o tipo ou causa
"""
class Acidentes:
	""" Causas de acidentes """
	def __init__(self):
		self.causa = ''
		self.tipo = ''
		self.quantidade_ocorrencias = 0

class AcidentesAno:
	""" Causas de acidentes separadas por ano"""
	def __init__(self):
		self.causa = ''
		self.tipo = ''
		self.quantidade_ocorrencias_list = []
		self.ano_list = []

class ProbabilidadeAcidentes:
	""" Probabilidade das causas de acidentes """
	def __init__(self):
		self.causa = ''
		self.tipo = ''
		self.probabilidade_por_limite_list = []

class MediaDesvioAcidentes:
	""" Media e desvios das causas de acidentes """
	def __init__(self):
		self.causa = ''
		self.tipo = ''
		self.media = 0.0
		self.desvio = 0.0