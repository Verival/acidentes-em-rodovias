# -*- coding: utf-8 -*- 

class Entidade():
        def __init__():
                pass

        def __str__():                
		attrs =vars(self)
		s= ''.join("%s: %s\n" % item for item in attrs.items())
		return s

class estadofisico(Entidade):
        def __init__(self):
                self.esid = 0
                self.estadofisico = ""

class causaacidente(Entidade):
        def __init__(self):
                self.tcacodigo = 0
                self.tcadescricao = ""

class ocorrencia(Entidade):
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

class corveiculo(Entidade):
        def __init__(self):
                self.tcecodigo = 0
                self.tcedescricao = ""
                self.tceatualiza = ""

class localbr(Entidade):
        def __init__(self):
                self.lbrid = 0
                self.lbruf = None
                self.lbrbr = ""
                self.lbrkm = 0
                self.lbraltitude = ""
                self.lbrlongitude = ""
                self.lbrpnvid = 0
                self.lbratualiza = ""

class uf(Entidade):
        def __init__(self):
                self.tufuf = ""
                self.tufdenominacao = ""

class marcadeveiculo(Entidade):
        def __init__(self):
                self.tmvcodigo = 0
                self.tmvdescricao = ""
                self.tmvatualiza = ""

class municipio(Entidade):
        def __init__(self):
                self.tmucodigo = 0
                self.tmudenominacao = ""
                self.tmuuf = ""

class ocorrenciaPessoa(Entidade):
        def __init__(self):
                self.opeid = 0
                self.opeocoid = None
                self.opepesid = None
                self.opeportenumero = ""
                self.opeportevalidade = ""
                self.opettecodigo = None
                self.openaoident = ""
                self.opeestrangeiro = ""
                self.opeanexo = ""
                self.opecondalegadas = ""
                self.sem = 0
                self.ano = 0
