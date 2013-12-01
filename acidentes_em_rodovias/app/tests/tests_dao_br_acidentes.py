# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from models.dao import br_acidentes_dao as dao
from models import br_acidentes
from _mysql_exceptions import OperationalError, ProgrammingError
from exception.internal_exceptions import *

class Test_BR_Acidentes(SimpleTestCase):
	def setUp(self):    #configura ambiente para teste
		self.estatistica = dao.BRAcidentesDAO()
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
		return "Teste da classe BRAcidentesDAO"

	def test_br_acidentes(self):
		self.assertIsNotNone(self.estatistica)

	def test_acidentes_br_geral(self):
		self.assertIsNotNone(self.estatistica.acidentes_br_geral())

	def test_acidentes_br_ano(self):
		br_acidentes_ano_list = self.estatistica.acidentes_br_ano()
		
		anos = br_acidentes_ano_list[0].ano_list
		self.assertEquals([2007, 2008, 2009, 2010, 2011, 2012, 2013], anos)

		brs = [i.br for i in br_acidentes_ano_list]
		self.assertIn('40', brs)