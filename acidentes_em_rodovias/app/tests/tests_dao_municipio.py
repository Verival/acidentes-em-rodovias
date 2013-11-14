# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from models.dao import generico_dao,uf_dao,ocorrencia_basica_dao,municipio_dao
from _mysql_exceptions import OperationalError, ProgrammingError
from exception.internal_exceptions import *

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