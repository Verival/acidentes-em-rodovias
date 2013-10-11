# -*- coding: utf-8 -*- 

class Ocorrencia():
	def __init__(self):
		self.ocoid = 0
		self.ocolocal = None
		self.ocostatus = ""
		self.ocomunicipio = None
		self.ocosentido = 0
		self.ocodataocorrencia = ""
		self.ocodataregistro = ""
		self.ocotipo = ""
		self.ococomid = None
		self.ocoidorigem = None
		self.ocodatafim = ""
		self.sem = 0
		self.ano = 0
	def __str__(self):
		attrs =vars(self)
		s= ''.join("%s: %s\n" % item for item in attrs.items())
		return s
		
