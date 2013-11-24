import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AcidentesRodoviasTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://127.0.0.1:8000/acidentes_rodovias')
        self.assertIn('Acidentes em Rodovias', self.browser.title)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)