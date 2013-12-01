# -*- encoding: utf8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class AcidentesRodoviasRegiaoTestCase(unittest.TestCase):
    porta = '8000'

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('http://127.0.0.1:'+self.porta+'/acidentes_rodovias/periodo')
        if (self.browser.title == u'Falha no carregamento da p\xe1gina'):
            print "\nInicie a aplicação na porta 8000 ou altere o atributo 'porta' no TestCase"
            exit(0)


    def test_pagetitle(self):
        self.assertIn('Acidentes em Rodovias', self.browser.title)
        
   
    def test_date_ate(self):
        self.browser.find_element_by_id('ate')


if __name__ == '__main__':
    unittest.main(verbosity=2)