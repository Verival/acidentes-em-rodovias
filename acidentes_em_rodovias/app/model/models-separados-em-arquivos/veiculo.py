# -*- coding: utf-8 -*-
from models import *
class veiculo(Entidade):
        def __init__(self):
                self.veiid = 0
                self.veiano = 0
                self.veitmvcodigo = marcadeveiculo()
                self.qtdocupantes = 0
                self.veitevcodigo = 0 
                self.veitcvcodigo = 0
                self.veitvvcodigo = tipoveiculo()
                self.veidescricao = ""
                self.veimunicipio = ""
                self.veitcecodigo = corveiculo()
                self.veimunorigem = ""
                self.veipaisorigem = 0
                self.veimundestino = ""
                self.veipaisdestino = 0
                self.veitttcodigo = 0
                self.veitipoproprietario = ""
                self.veiproprietario = 0
                self.veioenid = 0
                self.veisequencial = 0
                self.veitipoplaca = ""
