# -*- coding: utf-8 -*-

class CausasAcidentes:
	def __init__(self):
		self.causa = ''
		self.quantidade_ocorrencias = 0

	def __str__(self):
		return str(self.__dict__)

class CausasAcidentesAno:
	def __init__(self):
		self.causa = ''
		self.quantidade_ocorrencias_list = []
		self.ano_list = []

	def __str__(self):
		return str(self.__dict__)		

class ProbabilidadeCausasAcidentes:
	def __init__(self):
		self.causa = ''
		self.probabilidade_por_limite_list = []

	def __str__(self):
		return str(self.__dict__)		

class MediaDesvioCausasAcidentes:
	def __init__(self):
		self.causa = ''
		self.media = 0.0
		self.desvio = 0.0

	def __str__(self):
		return str(self.__dict__)		