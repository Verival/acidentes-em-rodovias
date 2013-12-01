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

class TestUF(SimpleTestCase):
	"""docstring for TestUF"""
	def setUp(self):    #configura ambiente para teste
		self.uf = uf_dao.UfDAO()
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
		return "Teste da classe GenericoDAO"

	def test_existing_uf_dao_instance(self):
		self.assertIsNotNone(self.uf)

	def test_list_uf(self):
		for i in self.uf.lista_ufs():
			self.assertIsNotNone(i)
		for i in self.uf.lista_ufs(limite=3):
			self.assertIsNotNone(str(i))
			self.assertIsNotNone(i)
