# -*- coding: utf-8 -*-

class OcorrenciaBasica:
	def __init__(self):
		self.ocoid = ''
		self.ocodataocorrencia = ''
		self.ocodataregistro = ''
		self.tmudenominacao = ''
		self.tmuuf = ''
		self.tcodescricao = ''
		self.ttadescricao = ''
		self.tcadescricao = ''
		self.lbrbr = ''
		self.tmvdescricao = ''
		self.tvvdescricao = ''

	def __str__(self):
		return str(self.__dict__)

		