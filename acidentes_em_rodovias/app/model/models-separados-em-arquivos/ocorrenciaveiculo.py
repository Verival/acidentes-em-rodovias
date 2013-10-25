# -*- coding: utf-8 -*-
from models import *
class ocorrenciaveiculo(Entidade):
        def __init__(self):
                self.ocvid = 0
                self.ocvocoid = ocorrencia()
                self.ocvveiid = veiculo()
