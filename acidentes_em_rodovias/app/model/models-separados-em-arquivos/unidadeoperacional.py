# -*- coding: utf-8 -*- 
from models import *
class unidadeoperacional(Entidade):
        def __init__(self):
                self.uniid = 0
                self.uniunidade = ""
                self.unilotacao = ""
                self.unisigla = ""
                self.unittucodigo = tipounidadeoperacional()
                #self.uniunidaderesponsavel = unidadeoperacional()
                self.uniunidaderesponsavel = 0
                self.unidenominacao = ""
                self.uniendereco = ""
                self.unimunicipio = municipio()
                self.unicep = ""
                self.unitelefone = ""
                self.uniemail = ""
                self.unilocal = ""
                self.unilatitude = ""
                self.unilongitude = ""
                self.unihelicoptero = ""
                self.unitexto = ""
