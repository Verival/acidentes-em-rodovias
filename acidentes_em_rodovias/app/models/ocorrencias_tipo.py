# -*- coding: utf-8 -*-

class OcorrenciasTipo:
	def __init__(self):
		self.ttadescricao = ''
		self.quantidade_ocorrencias = 0

	def __str__(self):
		return str(self.__dict__)

class OcorrenciasTipoAno:
	def __init__(self):
		self.ttadescricao = ''
		self.quantidade_ocorrencias_list = []
		self.ano_list = []

	def __str__(self):
		return str(self.__dict__)		

class ProbabilidadeTipo:
	def __init__(self):
		self.ttadescricao = ''
		self.probabilidade_por_limite_list = []

	def __str__(self):
		return str(self.__dict__)		