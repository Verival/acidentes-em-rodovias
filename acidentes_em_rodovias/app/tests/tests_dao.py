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

			
class TestTiposAcidentes(SimpleTestCase):
	"""docstring for TestUF"""
	def setUp(self):    #configura ambiente para teste
		self.dao = tipos_acidentes_dao.TiposAcidentesDAO()
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
		return "Teste da classe TestTiposAcidentesDAO"

	def test_tipos_acidentes(self):
		tipos_acidentes_list = self.dao.tipos_acidentes()
		
		self.assertEquals(len(tipos_acidentes_list), 16)

		descricao_tipos_acidentes = [i.tipo for i in tipos_acidentes_list]
		self.assertIn("Tombamento", descricao_tipos_acidentes)

	def test_tipos_acidentes_ano(self):
		tipos_acidentes_ano_list = self.dao.tipos_acidentes_ano()
		
		anos = tipos_acidentes_ano_list[0].ano_list
		self.assertEquals([2007, 2008, 2009, 2010, 2011, 2012, 2013], anos)

		descricao_tipos_acidentes_ano = [i.tipo for i in tipos_acidentes_ano_list]
		self.assertIn("Tombamento", descricao_tipos_acidentes_ano)

	def test_probabilidade_tipos_acidentes(self):
		probabilidade_tipos_acidentes_list = self.dao.probabilidade_tipos_acidentes()

		for probabilidade_tipos_acidentes in probabilidade_tipos_acidentes_list:
			for probabilidade in probabilidade_tipos_acidentes.probabilidade_por_limite_list:
				self.assertTrue(probabilidade >= 0 and probabilidade <= 100)

	def test_media_desvio_tipos_acidentes(self):
		media_desvio_tipos_acidentes_list = self.dao.media_desvio_tipos_acidentes()		

		for media_desvio_tipos_acidentes in media_desvio_tipos_acidentes_list:
			self.assertTrue(tipo_mais_acidentes.media > 0)
			self.assertTrue(tipo_mais_acidentes.desvio > 0)
			
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
