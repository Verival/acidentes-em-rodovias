# -*- coding: utf-8 -*-

class UFAcidentes():
	def __init__(self):
		self.uf = ''
		self.quantidade_ocorrencias = ''

	def __str__(self):
		return str(self.__dict__)

class UFAcidentesAno():
	def __init__(self):
		self.uf = ''
		self.quantidade_ocorrencias_list = []
		self.ano_list = []

	def __str__(self):
		return str(self.__dict__)