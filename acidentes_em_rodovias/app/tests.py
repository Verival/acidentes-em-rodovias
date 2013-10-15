# -*- coding: utf-8 -*- 

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import SimpleTestCase
import dao
        
class TestDAO(SimpleTestCase):
    
    def test_existing_DAO_instance(self):
        testDAO = dao.DAO('ocorrencia')
        self.assertIsNotNone(testDAO)
    
    def test_existing_possiblesDAOS_instance(self):
        testDAO = dao.DAO('ocorrencia')
        for keyDAO in testDAO.keys:
            possibleDAO = dao.DAO(keyDAO)
            self.assertIsNotNone(possibleDAO)
            
    def test_consulta_todos(self):
        testDAO = dao.DAO('ocorrencia')
        for keyDAO in testDAO.keys:
            possibleDAO = dao.DAO(keyDAO)
            self.assertIsNotNone(possibleDAO.consulta_todos(2))
            
    def test_troca_tabela(self):
        testDAO = dao.DAO('ocorrencia')
        for keyDAO in testDAO.keys:
            possibleDAO = dao.DAO(keyDAO)
            actualPossibleDAO = possibleDAO 
            changingPossibleDAO = possibleDAO.troca_tabela('causaacidente')
            self.assertIsNotNone(changingPossibleDAO)
            self.assertNotEquals(changingPossibleDAO, actualPossibleDAO)
     
