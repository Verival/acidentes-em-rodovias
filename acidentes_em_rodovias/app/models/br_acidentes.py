# -*- coding: utf-8 -*-

class BRAcidentes(object):
	def __init__(self):
			self.quantidade_ocorrencias = ''
			self.br = ''

	def __str__(self):
		return str(self.__dict__)

class BRAcidentesAno(object):
	def __init__(self):
			self.quantidade_ocorrencias_list = []
			self.br= ''
			self.ano_list = []

	def __str__(self):
		return str(self.__dict__)
