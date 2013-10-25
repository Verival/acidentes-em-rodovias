# -*- coding: utf-8 -*-
from models import *
class ocorrenciaacidente(Entidade):
        def __init__(self):
                self.oacocoid = 0
                self.oacttacodigo = tipoAcidente()
                self.oactcacodigo = causaacidente()
                self.oacdano =  ""
                self.oacdanoterc = ""
                self.oacdanoamb = ""
                self.oaclatitude = 0.0
                self.oaclongitude = 0.0
                self.oacdistab = 0.0
                self.oacdistac = 0.0
                self.oacdistbc = 0.0
                self.oacmodelopista = 0
                self.oacsentido1 = ""
                self.oacsentido2 = ""
                self.oacqtdfaixa1 = 0
                self.oacqtdfaixa2 = 0
                self.oacacostamento1 = ""
                self.oacacostamento2 = ""
                self.oaccanteiro = ""
                self.oaclinhacentral =  ""
                self.oacorientpista = ""
                self.oacgirafundo = ""
                self.oacversaocroqui = 0
                self.oacsitio = 0
                self.sem = 0
                self.ano = 0
