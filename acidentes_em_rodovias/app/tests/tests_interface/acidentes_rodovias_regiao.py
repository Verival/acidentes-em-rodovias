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
        self.browser.get('http://127.0.0.1:'+self.porta+'/acidentes_rodovias/regiao')
        if (self.browser.title == u'Falha no carregamento da p\xe1gina'):
            print "\nInicie a aplicação na porta 8000 ou altere o atributo 'porta' no TestCase"
            exit(0)


    def test_pagetitle(self):
        self.assertIn('Acidentes em Rodovias', self.browser.title)
        
    def test_estados_select(self):
        estados_list = ['Selecione um estado...', 'AC', 'AL', 'AP', 'AM', 'BA','CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 
            'MG', 'PB', 'PR', 'PA','PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

        for option in self.browser.find_elements_by_tag_name('option'):
            self.assertIn(option.get_attribute('value'), estados_list)
    
    def test_municipios_acre(self):
        municipios_list = [u'Selecione um munic\xedpio...', 'ACRELANDIA', 'ASSIS BRASIL', 'BRASILEIA', 'BUJARI', 'CAPIXABA',
            'CRUZEIRO DO SUL', 'EPITACIOLANDIA', 'MANOEL URBANO', 'PLACIDO DE CASTRO', 'PORTO ACRE', 
            'RIO BRANCO', 'SENA MADUREIRA', 'SENADOR GUIOMARD', 'XAPURI']
        
        self.browser.find_element_by_xpath("//option[@value='AC']")
        self.browser.find_element_by_id("btn_submit").click()

        for option in self.browser.find_elements_by_tag_name('option'):
            municipio_nome = option.get_attribute("text")
            self.assertIn(municipio_nome, municipios_list)

    def test_ocorrencias_acrelandia(self):
        br_excepected = '364'
        municipio_excepected = 'ACRELANDIA'
        uf_excepected = 'AC'

        resultados = self.browser.find_elements_by_xpath("//div[@class='resultados']")
        
        for resultado in resultados:
            br_test = resultado.find_element_by_class('br').get_attribute("text")
            self.assertEqual(br_test, br_excepected)

            municipio_test = resultado.find_element_by_class('municipio').get_attribute("text")
            self.assertEqual(municipio_test, municipio_excepected)

            uf_test = resultado.find_element_by_class('uf').get_attribute("text")
            self.assertEqual(uf_test, uf_excepected)


if __name__ == '__main__':
    unittest.main(verbosity=2)