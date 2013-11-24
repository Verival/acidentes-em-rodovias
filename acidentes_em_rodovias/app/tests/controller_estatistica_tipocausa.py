# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.template import RequestContext, TemplateDoesNotExist
from controller import estatisticas_controller as ctrl
from _mysql_exceptions import *

class TestTipoCausa(SimpleTestCase):
	"""docstring for TestController_Estatisticas"""
	def setUp(self):    #configura ambiente para teste
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
		sys.stderr.write('Done\n')
	
	def shortDescription(self):
		return "Teste da classe consultabasica_controller"
	
	def test_causas_acidentes(self):
		self.assertIsNotNone(ctrl.causas_acidentes(None))
