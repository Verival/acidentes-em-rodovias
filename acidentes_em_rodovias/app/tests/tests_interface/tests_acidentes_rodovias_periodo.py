# -*- encoding: utf8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import date

class AcidentesRodoviasPeriodoTestCase(unittest.TestCase):
    porta = '8080'
    mes = {'Janeiro' : 1, 'Fevereiro' : 2, 'Março' : 3, 'Abril' : 4, 'Maio' : 5, 'Junho' : 6, 'Julho' : 7, 
		    'Agosto' : 8, 'Setembro' : 9, 'Outubro' : 10, 'Novembro' : 11, 'Dezembro' : 12}

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('http://127.0.0.1:'+self.porta+'/acidentes_rodovias/periodo')
        if (self.browser.title == u'Falha no carregamento da p\xe1gina'):
            print "\nInicie a aplicação na porta"+self.porta+"ou altere o atributo 'porta' no TestCase"
            exit(0)


    def test_pagetitle(self):
        self.assertIn('Acidentes em Rodovias', self.browser.title)
        
   
    def test_date_periodo_invalido(self):
	de = '12345678'
	ate = '23456789'
        campo_de = self.browser.find_element_by_id('de')
	campo_ate = self.browser.find_element_by_id('ate')
	
	campo_de.send_keys(de)
	campo_ate.send_keys(ate)

	self.browser.find_element_by_id('btn_submit').click()	

	modal_error = self.browser.find_element_by_id('modalErro')

	self.assertIsNotNone(modal_error)

    def test_date_periodo_valido(self):
	    de = '12/04/2008'
	    ate = '30/06/2008'

	    campo_de = self.browser.find_element_by_id('de')
	    campo_ate = self.browser.find_element_by_id('ate')

	    campo_de.send_keys(de)
	    campo_ate.send_keys(ate)

	    self.browser.find_element_by_id('btn_submit').click()

	    result_list = self.browser.find_elements_by_class_name('resultados')

	    self.assertIsNotNone(result_list)

    def test_verifica_periodo(self):
	    de = '12/04/2008'
	    ate = '30/06/2008'

	    campo_de = self.browser.find_element_by_id('de')
	    campo_ate = self.browser.find_element_by_id('ate')

	    campo_de.send_keys(de)
	    campo_ate.send_keys(ate)

	    de = de.split('/')
	    ate = ate.split('/')

	    de = date(int(de[2]), int(de[1]), int(de[0]))
	    ate = date(int(ate[2]), int(ate[1]), int(ate[0]))

	    self.browser.find_element_by_id('btn_submit').click()

	    result_list = self.browser.find_elements_by_class_name('data_registro')

	    for element in result_list:
		    data_registro = element.text
		    data_registro = data_registro.split()
		    data_registro = date(int(data_registro[4]), self.mes.get(data_registro[2]), int(data_registro[0]))
		    self.assertTrue(de <= data_registro <= ate)

if __name__ == '__main__':
    unittest.main(verbosity=2)
