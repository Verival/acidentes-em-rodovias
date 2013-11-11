# -*- coding: utf-8 -*-
from exceptions import Exception

class NoPandasComponentError(Exception):
	"""docstring for NoPandasComponentError"""
	def __init__(self, message):
		Exception.__init__(self)
		self.message = message
	def __str__(self):
		return self.message
