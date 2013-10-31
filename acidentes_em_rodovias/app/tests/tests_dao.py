# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from model.dao import generico_dao
        
class TestDAO(SimpleTestCase):
    
    def test_existing_generico_dao_instance(self):
        print 'Testing existing GenericoDAO instance...'

        test_dao = GenericoDAO()
        self.assertIsNotNone(test_dao)

        print '\t- Test complete'
    
    def test_existing_possiblesDAOS_instance(self):
        testDAO = dao.DAO('ocorrencia')
        for keyDAO in testDAO.keys:
            possibleDAO = dao.DAO(keyDAO)
            self.assertIsNotNone(possibleDAO)
            
