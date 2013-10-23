# -*- coding: utf-8 -*-
from models import *
class ocorrenciaPessoa(Entidade):
        def __init__(self):
                self.opeid = 0
                self.opeocoid = ocorrencia()
                self.opepesid = pessoa()
                self.opeportenumero = ""
                self.opeportevalidade = ""
                self.opettecodigo = tipoenvolvido()
                self.openaoident = ""
                self.opeestrangeiro = ""
                self.opeanexo = ""
                self.opecondalegadas = ""
                self.sem = 0
                self.ano = 0
