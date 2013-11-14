# -*- coding: utf-8 -*-

class EnvolvidosAcidente:
	def __init__(self):
		self.quantidade_envolvidos = 0
		self.quantidade_acidentes = 0
		self.ano = 0

	def __str__(self):
		return str(self.__dict__)