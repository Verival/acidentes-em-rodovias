# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.template import RequestContext, TemplateDoesNotExist
from controller import consultabasica_controller as ctrl
from _mysql_exceptions import *
from nose import with_setup
from mock import MagicMock,patch,Mock
from django.utils.datastructures import MultiValueDictKeyError

class Test_Periodo(SimpleTestCase):
	"""docstring for TestController_Consulta_Basica"""
	def setUp(self):    #configura ambiente para teste
		self.request     = Mock()
		self.request.GET = MagicMock(side_effect=KeyError(MultiValueDictKeyError),return_value='DF')
		#descobre qual metodo será chamado e formata a saída
		func = str(self.id).split('=')[-1][:-2]
		func = func.split('test_')[-1]
		func = func.replace('_',' ')
		out = '\rTeste de ' + func + ' '
		out = out.ljust(65,'-')
		sys.stderr.write(out)
		self.shortDescription()

	def tearDown(self):
		# informa que o teste foi realizado
		#print 'Done'                                
		sys.stderr.write('Done\n')
	
	def shortDescription(self):
		return "Teste da classe consultabasica_controller"

	def test_consulta_por_regiao(self):
		ctrl.consulta_por_regiao(None)

	def test_consulta_municipios_na_regiao(self):
		with self.assertRaises(TypeError):
			ctrl.consulta_municipios_na_regiao(self.request)

	def test_consulta_por_periodo(self):
		self.assertIsNotNone(ctrl.consulta_por_periodo(None))
		
	def test_consulta_ocorrencias_por_periodo(self):
		with self.assertRaises(AttributeError):
			self.assertIsNotNone(ctrl.consulta_ocorrencias_por_periodo(None))
