# -*- coding: utf-8 -*-
"""@package UF dos acidentes
Declaração das classes para os acitendes e suas UF.

Este modulo contem as classe para modelo dos Acidentes com suas UF
"""

class UFAcidentes():
	""" UF dos acidentes """
	def __init__(self):
		self.uf = ''
		self.quantidade_ocorrencias = ''
		self.latitude = 0.0
		self.longitude = 0.0

class UFAcidentesAno():
	""" UF dos acidentes separados por ano """
	def __init__(self):
		self.uf = ''
		self.quantidade_ocorrencias_list = []
		self.ano_list = []