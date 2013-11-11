# -*- coding: utf-8 -*-

class EstatisticaPessoas:
	def __init__(self):
		self.ano = ''
		self.sexo = ''
		self.quantidade = ''

	def __str__(self):
		return str(self.__dict__)