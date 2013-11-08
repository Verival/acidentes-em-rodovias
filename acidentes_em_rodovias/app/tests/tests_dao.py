# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from models.dao import generico_dao,uf_dao,ocorrencia_basica_dao,municipio_dao

#----------------------DAO----------------------------------
class TestDAO(SimpleTestCase):
	"""docstring for TestDAO"""
	def setUp(self):    #configura ambiente para teste
		self.dao = generico_dao.GenericoDAO()
		#descobre qual metodo será chamado e formata a saída
		func = str(self.id).split('=')[-1][:-2]
		func = func.split('test_')[-1]
		func = func.replace('_',' ')
		out = '\rTeste de ' + func + ' '
		print out.ljust(65,'-'),
		self.shortDescription()

	def tearDown(self):
		# informa que o teste foi realizado
		print 'Done'                                
	
	def shortDescription(self):
		return "Teste da classe GenericoDAO"

	def test_existing_dao_instance(self):
		self.assertIsNotNone(self.dao)
		
	def test_get_conexao(self):
		self.dao.database = ' '
		self.dao.usuario = ' '
		self.dao.senha = ' '
		self.dao.host = ' '
		self.assertIsNone(self.dao.get_conexao())
		
	def test_try_query(self):
		self.dao.conexao = ''
		self.assertIsNone(self.dao.executa_query("show tables;"))

	def test_transforma_objeto(self):
		#Quando tudo funciona bem
		query='SELECT tufuf, tufdenominacao FROM uf ORDER BY tufdenominacao LIMIT 3;'
		self.assertIsNotNone(self.dao.transforma_dicionario_em_objetos(self.dao.executa_query(query),'Uf','uf'))
		#Testa exception
		self.assertIsNone(self.dao.transforma_dicionario_em_objetos(None,'Uf','uf'))
		
	

#----------------------UF-----------------------------------
class TestUF(SimpleTestCase):
	"""docstring for TestUF"""
	def setUp(self):    #configura ambiente para teste
		self.uf = uf_dao.UfDAO()
		#descobre qual metodo será chamado e formata a saída
		func = str(self.id).split('=')[-1][:-2]
		func = func.split('test_')[-1]
		func = func.replace('_',' ')
		out = '\rTeste de ' + func + ' '
		print out.ljust(65,'-'),
		self.shortDescription()

	def tearDown(self):
		# informa que o teste foi realizado
		print 'Done'                       

	def shortDescription(self):
		return "Teste da classe GenericoDAO"

	def test_existing_uf_dao_instance(self):
		self.assertIsNotNone(self.uf)

	def test_list_uf(self):
		for i in self.uf.lista_ufs():
			self.assertIsNotNone(i)
		for i in self.uf.lista_ufs(limite=3):
			self.assertIsNotNone(str(i))
			self.assertIsNotNone(i)

#----------------------Ocorrencia-----------------------------------
class TestOcorrencia(SimpleTestCase):
	"""docstring for TestOcorrencia"""
	def setUp(self):    #configura ambiente para teste
		self.ocorrencia = ocorrencia_basica_dao.OcorrenciaBasicaDAO()
		#descobre qual metodo será chamado e formata a saída
		func = str(self.id).split('=')[-1][:-2]
		func = func.split('test_')[-1]
		func = func.replace('_',' ')
		out = '\rTeste de ' + func + ' '
		print out.ljust(65,'-'),
		self.shortDescription()

	def tearDown(self):
		# informa que o teste foi realizado
		print 'Done'                       

	def shortDescription(self):
		return "Teste da classe OcorrenciaBasica"

	def test_existing_ocorrencia_dao_instance(self):
		self.assertIsNotNone(self.ocorrencia)

	def test_ocorrencia_por_regiao(self):
		# 97012 = Brasilia
		oco =  self.ocorrencia.lista_ocorrencias_por_regiao(97012)
		self.assertIsNotNone(oco)   #verifica se não retorna nulo
		oco =  self.ocorrencia.lista_ocorrencias_por_regiao(97012,limite=3)
		self.assertIsNotNone(oco)   #verifica se não retorna nulo
		self.assertLess(len(oco),4) #verifica se retorna no maximo 3 ocorrencias
		for i in oco:               #verifica se todos os retornos estão no DF
			self.assertIsNotNone(str(i))
			self.assertEqual(i.tmuuf, 'DF')


	def test_ocorrencia_por_periodo(self):
		oco =  self.ocorrencia.lista_ocorrencias_por_periodo('06/01/06','06/12/06')
		self.assertIsNotNone(oco)   #verifica se não retorna nulo
		oco =  self.ocorrencia.lista_ocorrencias_por_periodo('06/01/06','06/12/06',limite=3)
		self.assertIsNotNone(oco)   #verifica se não retorna nulo
		self.assertLess(len(oco),4) #verifica se retorna no maximo 3 ocorrencias
		for i in oco:               #verifica se as ocorrencias aconteceram em 2006
			self.skipTest("Tabela ainda não alterada nas demais máquinas")
			self.assertEqual(2006, i.ocodataocorrencia.year)
			
#----------------------MUNICIPIO-----------------------------------
class TestMunicipio(SimpleTestCase):
	"""docstring for TestMunicipio"""
	def setUp(self):    #configura ambiente para teste
		self.municipio = municipio_dao.MunicipioDAO()
		#descobre qual metodo será chamado e formata a saída
		func = str(self.id).split('=')[-1][:-2]
		func = func.split('test_')[-1]
		func = func.replace('_',' ')
		out = '\rTeste de ' + func + ' '
		print out.ljust(65,'-'),
		self.shortDescription()

	def tearDown(self):
		# informa que o teste foi realizado
		print 'Done'                       

	def shortDescription(self):
		return "Teste da classe MunicipioDAO"

	def test_existing_municipio_dao_instance(self):
		self.assertIsNotNone(self.municipio)

	def test_list_municipio(self):
		for i in self.municipio.lista_municipios("DF"):
			self.assertIsNotNone(i)
		for i in self.municipio.lista_municipios("DF", limite=3):
			self.assertIsNotNone(str(i))
			self.assertIsNotNone(i)
			
# #----------------------URLs-----------------------------------
# from django.test import TestCase
# class TestMyViews(TestCase):
# 	def setUp(self):    #configura ambiente para teste
# 		self.client = self.client_class()
# 		#descobre qual metodo será chamado e formata a saída
# 		func = str(self.id).split('=')[-1][:-2]
# 		func = func.split('test_')[-1]
# 		func = func.replace('_',' ')
# 		out = '\rTeste de ' + func + ' '
# 		print out.ljust(65,'-'),
# 		self.shortDescription()

# 	def tearDown(self):
# 		# informa que o teste foi pulado
# 		print 'Skiped!'  

# 	def shortDescription(self):
# 		print "Teste das URLs"

# 	def test_urls(self):
# 		self.skipTest("Testes de URLs ainda incompleto")
# 		self.assertIsNotNone(self.client.get('acidentes_rodovias/'))	#Tenta fazer uma conexão usando cliente padrão
