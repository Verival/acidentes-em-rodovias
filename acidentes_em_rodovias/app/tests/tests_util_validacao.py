# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.template import RequestContext, TemplateDoesNotExist
from exception.validation_exceptions import ParametroInseguroClienteError, DataInvalidaError
from util import validacao_util
from _mysql_exceptions import *

class Test_Valida(SimpleTestCase):
	"""docstring for Test_Valida"""
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
		return "Teste da classe Test_Valida"
	
	def test_valida_data(self):
		self.assertFalse(validacao_util.valida_data("10/10/2013"))
		with self.assertRaises(DataInvalidaError):
			self.assertFalse(validacao_util.valida_data("20 de março de 2013"))
			
	def test_valida_caracteres(self):
		with self.assertRaises(ParametroInseguroClienteError):
			self.assertIsNone(validacao_util.valida_caracteres(None))
		with self.assertRaises(ParametroInseguroClienteError):
			self.assertFalse(validacao_util.valida_caracteres("./$%^&"))
