# -*- coding: utf-8 -*-

class BRAcidentes(object):
	def __init__(self):
			self.quantidade_ocorrencias = ''
			self.br = ''

	def __str__(self):
		return str(self.__dict__)

class BRAcidentesAno(object):
	def __init__(self):
			self.quantidade_ocorrencias = ''
			self.br = ''
			self.ano = ''

	def __str__(self):
		return str(self.__dict__)
