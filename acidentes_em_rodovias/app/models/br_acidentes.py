# -*- coding: utf-8 -*-
"""@package Modelo de acidentes
Declaração das classes para acidentes.

Este modulo contem declação das classes de modelo
para acidentes em BRs
"""
class BRAcidentes(object):
	""" Acidentes em geral das rodovias"""
	def __init__(self):
			self.quantidade_ocorrencias = ''
			self.br = ''

class BRAcidentesAno(object):
	""" Acidentes em geral das rodovias separados por ano"""
	def __init__(self):
			self.quantidade_ocorrencias_list = []
			self.br= ''
			self.ano_list = []