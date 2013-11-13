# -*- coding: utf-8 -*-

class TiposAcidentes:
	def __init__(self):
		self.tipo = ''
		self.quantidade_ocorrencias = 0

	def __str__(self):
		return str(self.__dict__)

class TiposAcidentesAno:
	def __init__(self):
		self.tipo = ''
		self.quantidade_ocorrencias_list = []
		self.ano_list = []

	def __str__(self):
		return str(self.__dict__)		

class ProbabilidadeTiposAcidentes:
	def __init__(self):
		self.tipo = ''
		self.probabilidade_por_limite_list = []

	def __str__(self):
		return str(self.__dict__)		

class MediaDesvioTiposAcidentes:
	def __init__(self):
		self.tipo = ''
		self.media = 0.0
		self.desvio = 0.0

	def __str__(self):
		return str(self.__dict__)		