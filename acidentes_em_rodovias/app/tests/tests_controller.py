# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from django.template import RequestContext, TemplateDoesNotExist
from controller import consultabasica_controller as ctrl

#----------------------DAO----------------------------------
class TestController_Consulta_Basica(SimpleTestCase):
	"""docstring for TestController_Consulta_Basica"""
	def setUp(self):    #configura ambiente para teste

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
		return "Teste da classe consultabasica_controller"

	def test_render_to_response(self):
		self.assertIsNotNone( ctrl.render_to_response("index.html", context_instance=RequestContext(None)) )
		with self.assertRaises(TemplateDoesNotExist):
			ctrl.render_to_response("nao_existo", context_instance=RequestContext(None))

	def test_index(self):
		#help(SimpleTestCase)
		#help(ctrl.render_to_response)
		self.assertIsNotNone( ctrl.index(None))

	def test_consulta_por_regiao(self):
		self.assertIsNotNone(ctrl.consulta_por_regiao(None))
		
		
