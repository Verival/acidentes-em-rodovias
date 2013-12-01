# -*- coding: utf-8 -*-
"""@package validation exceptions
Exceções de validação.

Este modulo contem classes de controle de exceção
"""
from exceptions import Exception

class DataInvalidaError(Exception):
	"""docstring for InvalidDateError"""
	def __init__(self, message):
		Exception.__init__(self)
		self.message = message
	def __str__(self):
		return self.message

class ParametroInseguroClienteError(Exception):
	"""docstring for InvalidParameterError"""
	def __init__(self, message):
		Exception.__init__(self)
		self.message = message
	def __str__(self):
		return self.message