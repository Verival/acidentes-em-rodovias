# -*- coding: utf-8 -*-
"""@package Modelo de causas de acidentes
Declaração das classes para causas de acidentes.

Este modulo contem declação das classes de modelo
para acidentes contendo o tipo da causa
"""
class CausasAcidentes:
	""" Causas de acidentes """
	def __init__(self):
		self.causa = ''
		self.quantidade_ocorrencias = 0

class CausasAcidentesAno:
	""" Causas de acidentes separadas por ano"""
	def __init__(self):
		self.causa = ''
		self.quantidade_ocorrencias_list = []
		self.ano_list = []

class ProbabilidadeCausasAcidentes:
	""" Probabilidade das causas de acidentes """
	def __init__(self):
		self.causa = ''
		self.probabilidade_por_limite_list = []

class MediaDesvioCausasAcidentes:
	""" Media e desvios das causas de acidentes """
	def __init__(self):
		self.causa = ''
		self.media = 0.0
		self.desvio = 0.0