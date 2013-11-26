# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from models.dao import uf_dao, causas_acidentes_dao, ocorrencia_basica_dao, causas_acidentes_dao, municipio_dao, generico_dao
from _mysql_exceptions import OperationalError, ProgrammingError
from exception.internal_exceptions import *

class TestCausasAcidentes(SimpleTestCase):
	"""docstring for TestUF"""
	def setUp(self):    #configura ambiente para teste
		self.dao = causas_acidentes_dao.CausasAcidentesDAO()
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
		return "Teste da classe TestCausasAcidentesDAO"

	def test_causas_acidentes(self):
		causas_acidentes_list = self.dao.causas_acidentes()
		
		#self.assertEquals(len(causas_acidentes_list), 16)

		descricao_causas_acidentes = [i.causa for i in causas_acidentes_list]
		self.assertIn("Outras", descricao_causas_acidentes)

	def test_causas_acidentes_ano(self):
		causas_acidentes_ano_list = self.dao.causas_acidentes_ano()
		
		anos = causas_acidentes_ano_list[0].ano_list
		self.assertEquals([2007, 2008, 2009, 2010, 2011, 2012, 2013], anos)

		descricao_causas_acidentes_ano = [i.causa for i in causas_acidentes_ano_list]
		self.assertIn("Outras", descricao_causas_acidentes_ano)

	def test_probabilidade_causas_acidentes(self):
		probabilidade_causas_acidentes_list = self.dao.probabilidade_causas_acidentes()

		for probabilidade_causas_acidentes in probabilidade_causas_acidentes_list:
			for probabilidade in probabilidade_causas_acidentes.probabilidade_por_limite_list:
				self.assertTrue(probabilidade >= 0 and probabilidade <= 100)

	def test_media_desvio_causas_acidentes(self):
		media_desvio_causas_acidentes_list = self.dao.media_desvio_causas_acidentes()		

		for media_desvio_causas_acidentes in media_desvio_causas_acidentes_list:
			self.assertTrue(media_desvio_causas_acidentes.media > 0)
			self.assertTrue(media_desvio_causas_acidentes.desvio > 0)
