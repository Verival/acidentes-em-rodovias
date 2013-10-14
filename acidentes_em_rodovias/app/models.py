# -*- coding: utf-8 -*- 

class Entidade():
        def __init__(self):
                pass

        def __str__(self):                
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
		self.ocolocal = localbr()
		self.ocostatus = ""
		self.ocomunicipio = municipio()
		self.ocosentido = 0
		self.ocodataocorrencia = ""
		self.ocodataregistro = ""
		self.ocotipo = ""
		self.ococomid = tipocomunicacao()
		self.ocoidorigem = ocorrencia()
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
                self.lbruf = uf()
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

class ocorrenciaacidente(Entidade):
        def __init__(self):
                self.oacocoid = 0
                self.oacttacodigo = tipoacidente()
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

class ocorrenciaveiculo(Entidade):
        def __init__(self):
                self.ocvid = 0
                self.ocvocoid = ocorrencia()
                self.ocvveiid = veiculo()

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

class tipoAcidente(Entidade):
        def __init__(self):
                self.ttacodiggo = 0
                self.ttadescricao = ""
                self.ttaatualiza = ""
                self.ttarelacidente = ""
                self.ttaativo = ""

class tipoComunicacao(Entidade):
        def __init__(self):
                self.tcocodigo = 0
                self.tcodescricao = ""
                self.tcoatualiza = ""

class tipoenvolvido(Entidade):
        def __init__(self):
                self.ttecodigo = 0
                self.ttedescricao = ""
                self.tteatualiza = ""
                self.tteativo = ""

class tipolocalidade(Entidade):
        def __init__(self):
                self.ttlcodigo = 0
                self.ttldescricao = ""
                self.ttlatualiza = ""

class tipounidadeoperacional(Entidade):
        def __init__(self):
                self.ttucodigo = 0
                self.ttudescricao = ""
                self.ttuatualiza = ""

class tipoveiculo(Entidade):
        def __init__(self):
                self.tvvcodigo = 0
                self.tvvdescricao = ""
                self.tvvatualiza = ""
                self.tvvrelacidente = ""
                self.tvvativo = ""

class unidadeoperacional(Entidade):
        def __init__(self):
                self.uniid = 0
                self.uniunidade = ""
                self.unilotacao = ""
                self.unisigla = ""
                self.unittucodigo = tipounidadeoperacional()
                self.uniunidaderesponsavel = unidadeoperacional()
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
