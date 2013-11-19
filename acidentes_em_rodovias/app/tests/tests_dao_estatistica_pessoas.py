# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from models.dao import estatistica_pessoas_dao as dao
from models import pessoas_acidentes
from _mysql_exceptions import OperationalError, ProgrammingError
from exception.internal_exceptions import *

class Test_Estatistica_Pessoa(SimpleTestCase):
	"""docstring for Test_Estatistica_Pessoa
	"""
	def setUp(self):    #configura ambiente para teste
		self.estatistica = dao.EstatisticaPessoasDAO()
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
		return "Teste da classe EstatisticasPessoasDAO"

	def test_acidentes_por_sexo(self):
		self.assertIsNotNone(self.estatistica)

	def test_instancia_estatistica_pessoa(self):
		with self.assertRaises(NameError):
			self.assertIsNotNone(estatistica_pessoas.EstatisticaPessoas())
			self.assertIsNotNone(str(estatistica_pessoas.EstatisticaPessoas()))
