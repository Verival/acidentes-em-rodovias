# -*- coding: utf-8 -*-
"""@package internal exceptions
Exceções de validações internas.

Este modulo contem classes de controle de exceção 
para validações internas
"""
from exceptions import Exception

class ResultadoConsultaNuloError(Exception):
	"""docstring for ResultadoConsultaNuloError"""
	def __init__(self, message):
		""" Initialize module """
		Exception.__init__(self)
		self.message = message
	def __str__(self):
		""" How module shold be printed """
		return self.message
