# -*- coding: utf-8 -*-
from models import *
class pessoa(Entidade):
        def __init__(self):
                self.pesid = 0
                self.pesdatanascimento = ""
                self.pesnaturalidade = ""
                self.pesnacionalidade = ""
                self.pessexo = ""
                self.pesteccodigo = 0
                self.pestgicodigo = 0
                self.pesmunicipio = municipio()
                self.pestopcodigo = ""
                self.pesmunicipioori = ""
                self.pespaisori = ""
                self.pesmunicipiodest = ""
                self.pespaisdest = ""
                self.pesveiid = veiculo()
                self.pesestadofisico = estadofisico()
                self.pescinto = ""
                self.pescapacete = ""
                self.peshabilitado = ""
                self.pesscorrido = ""
                self.pesdormindo = ""
                self.pesalcool = ""
                self.peskmpercorre = ""
                self.peshorapercorre = ""
                self.pescategcnh = ""
                self.pesufcnh = ""
                self.pespaiscnh = ""
                self.pesdatahabil = ""
                self.pesdatavalidade = ""
                self.pesidade = ""
                self.pesaltura = ""
                self.pespeso = ""
                self.pescicatriz = ""
                self.pestatuagem = ""
                self.pessinal = ""
                self.peslesao = ""
                self.pestcccodigo = ""
                self.pestctcodigo = ""
                self.pestclcodigo = ""
                self.pesoenid = ""
