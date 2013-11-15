# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from controller import consultabasica_controller
from _mysql_exceptions import OperationalError, ProgrammingError
from exception.internal_exceptions import *


#----------------------DAO----------------------------------
class TestControllerRegiao(SimpleTestCase):
	"""docstring for TestDAO"""
	def setUp(self):    #configura ambiente para teste
		self.ctrl = consultabasica_controller()
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

	def test_instancia_controller_regiao(self):
		self.assertIsNotNone(self.ctrl)

	def test_consulta_regiao(self):
		self.assertIsNotNone(self.ctrl.consulta_por_regiao(None))