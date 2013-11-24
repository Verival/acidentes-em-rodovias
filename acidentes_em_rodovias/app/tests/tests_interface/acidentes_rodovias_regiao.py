import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AcidentesRodoviasRegiaoTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('http://127.0.0.1:8000/acidentes_rodovias/regiao')

    def testPageTitle(self):
        self.assertIn('Acidentes em Rodovias', self.browser.title)
        
    def testDropDownAcre(self):
        dropDown = self.browser.find_element_by_class_name('current')
        self.assertIn('Acre', dropDown.text)
        
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)