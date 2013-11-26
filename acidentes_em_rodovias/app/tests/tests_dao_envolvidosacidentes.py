# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from models.dao import uf_dao, tipos_acidentes_dao, ocorrencia_basica_dao, causas_acidentes_dao, municipio_dao, generico_dao, envolvidos_acidentes_dao
from _mysql_exceptions import OperationalError, ProgrammingError
from exception.internal_exceptions import *
from datetime import datetime

class TestEnvolvidosAcidentes(SimpleTestCase):
	"""docstring for TestUF"""
	def setUp(self):	#configura ambiente para teste
		self.dao = envolvidos_acidentes_dao.EnvolvidosAcidentesDAO()
		#descobre qual método será chamado e formata a saída
		func = str(self.id).split('=')[-1][:-2]
		func = func.split('test_')[-1]
		func = func.replace('_', ' ')
		out = '\rTeste de ' + func + ' '
		out = out.ljust(65,'-')
		sys.stderr.write(out)
		self.shortDescription()

	def tearDown(self):
		#informa que o teste foi realizado
		sys.stderr.write('Done\n')

	def shortDescription(self):
		return "Teste da classe TestEnvolvidosAcidentesDAO"

	def test_envolvidos_acidentes(self):
		envolvidos_acidentes_list = self.dao.envolvidos_acidentes()
		
		self.assertIsNotNone(envolvidos_acidentes_list)

		diffyears = datetime.now().year - 2007

		self.assertEquals(len(envolvidos_acidentes_list), diffyears + 1)

	def test_media_desvio_envolvidos(self):
		lista_medias, desvio = self.dao.media_desvio_envolvidos()

		self.assertIsNotNone(lista_medias)
		self.assertIsNotNone(desvio)
