# -*- coding: utf-8 -*-

class TiposAcidentes:
	def __init__(self):
		self.tipo = ''
		self.quantidade_ocorrencias = 0

class TiposAcidentesAno:
	def __init__(self):
		self.tipo = ''
		self.quantidade_ocorrencias_list = []
		self.ano_list = []

class ProbabilidadeTiposAcidentes:
	def __init__(self):
		self.tipo = ''
		self.probabilidade_por_limite_list = []	

class MediaDesvioTiposAcidentes:
	def __init__(self):
		self.tipo = ''
		self.media = 0.0
		self.desvio = 0.0