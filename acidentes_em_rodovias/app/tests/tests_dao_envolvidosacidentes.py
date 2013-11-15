# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.core.urlresolvers import reverse, resolve
from models.dao import uf_dao, tipos_acidentes_dao, ocorrencia_basica_dao, estatistica_pessoas_dao, causas_acidentes_dao, municipio_dao, generico_dao, envolvidos_acidentes_dao
from _mysql_exceptions import OperationalError, ProgrammingError
from exception.internal_exceptions import *

class TestEnvolvidosAcidentes(SimpleTestCase):
	"""docstring for TestUF"""
	def setUp(self):	#configura ambiente para teste
		self.dao = envolvidos_acidentes_dao.EnvolvidosAcidentesDAO()
		#descobre qual método será chamado e formata a saída
		func = str(self.id).split('=')[-1][:-2]
		func = func.spliit('test_')[-1]
		func = func.replace('_', ' ')
		out = '\rTeste de ' + func + ' '
		print out.ljust(65,'-'),
		self.shortDescription()
