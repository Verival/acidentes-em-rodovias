# -*- encoding: utf8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class AcidentesRodoviasRegiaoTestCase(unittest.TestCase):
    porta = '8080'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('http://127.0.0.1:'+self.porta+'/acidentes_rodovias/periodo')
        if (self.browser.title == u'Falha no carregamento da p\xe1gina'):
            print "\nInicie a aplicação na porta 8000 ou altere o atributo 'porta' no TestCase"
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

if __name__ == '__main__':
    unittest.main(verbosity=2)
