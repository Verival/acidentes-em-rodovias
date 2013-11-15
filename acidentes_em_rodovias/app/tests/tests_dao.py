# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from models.dao import uf_dao, tipos_acidentes_dao, ocorrencia_basica_dao, estatistica_pessoas_dao, causas_acidentes_dao, municipio_dao, generico_dao
from _mysql_exceptions import OperationalError, ProgrammingError
from exception.internal_exceptions import *

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
		#self.assertIsNone(self.dao.get_conexao())
		with self.assertRaises(OperationalError):
			self.dao.get_conexao()

	def test_try_query(self):
		with self.assertRaises(ProgrammingError):
			self.assertIsNone(self.dao.executa_query("showjik;"))

	def test_transforma_objeto(self):
		#Quando tudo funciona bem
		query="SELECT tufuf, tufdenominacao FROM uf WHERE tufuf = 'DF' ORDER BY tufdenominacao;"
		#Testa se passa no 'if' e 'else' do for
		ufList = self.dao.transforma_dicionario_em_objetos(self.dao.executa_query(query),'Uf','uf')
		self.assertEquals(ufList[0].tufuf , 'DF')
		#Testa se a lista nao esta vazia.
		self.assertIsNotNone(self.dao.transforma_dicionario_em_objetos(self.dao.executa_query(query),'Uf','uf'))
		#Testa exception
		with self.assertRaises(ResultadoConsultaNuloError):
			self.assertIsNone(self.dao.transforma_dicionario_em_objetos(None,'Uf','uf'))
			
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
