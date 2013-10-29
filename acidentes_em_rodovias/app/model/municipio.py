# -*- coding: utf-8 -*-

class Municipio():
	def __init__(self):
		self.tmucodigo = ''
		self.tmudenominacao = ''
		self.tmuuf = ''
	
	def __str__(self):
		return str(self.__dict__)
