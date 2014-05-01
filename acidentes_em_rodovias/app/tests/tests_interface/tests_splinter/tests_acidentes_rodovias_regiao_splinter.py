import unittest
from splinter import Browser
import time
import sys

class AcidentesRodoviasRegiaoTestCase(unittest.TestCase):
	
	def setUp(self):
		self.browser = Browser()
		self.browser.visit('http://127.0.0.1:8000/acidentes_rodovias/')

		
	def tearDown(self):
		self.browser.quit()
		sys.stderr.write('Done\n')

	def test_pagetitle(self):
		self.assertIn('Acidentes em Rodovias', self.browser.title)

	def test_estados_select(self):
    	#estados_list = ['Selecione um estado...', 'AC', 'AL', 'AP', 'AM', 'BA',
    	#'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PB', 'PR', 'PA','PE', 
    	#'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    	#for option_list in self.browser.find_by_tag('option'):
    		self.assertIn(option_list.find_by_name('value'), estados_list)


if __name__ == '__main__':
    unittest.main(verbosity=2)


# browser = Browser()
# browser.visit('http://google.com')
# browser.fill('q', 'splinter - python acceptance testing for web applications')
# browser.find_by_name('btnG').click()

# if browser.is_text_present('splinter.cobrateam.info'):
#     print "Yes, the official website was found!"
# else:
#     print "No, it wasn't found... We need to improve our SEO techniques"

# browser.quit()