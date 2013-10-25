# -*- coding: utf-8 -*-
from models import *
class ocorrencia(Entidade):
	def __init__(self):
		self.ocoid = 0
		self.ocolocal = localbr()
		self.ocostatus = ""
		self.ocomunicipio = municipio()
		self.ocosentido = 0
		self.ocodataocorrencia = ""
		self.ocodataregistro = ""
		self.ocotipo = ""
		self.ococomid = tipocomunicacao()
		#self.ocoidorigem = ocorrencia()
		self.ocoidorigem = 0
		self.ocodatafim = ""
		self.sem = 0
		self.ano = 0
