# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from models.dao import generico_dao,uf_dao

#----------------------DAO----------------------------------
class TestDAO(SimpleTestCase):
    """docstring for TestDAO"""
    def setUp(self):    #configura ambiente para teste
        self.dao = generico_dao.GenericoDAO()
        #descobre qual metodo será chamado e formata a saída
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_',' ')
        out = '\rTeste de ' + func + ' '
        print out.ljust(65,'-'),

    def tearDown(self):
        # informa que o teste foi realizado
        print 'Done'                                
    
    def shortDescription(self):
        print "Teste da classe GenericoDAO"

    def test_existing_dao_instance(self):
        self.assertIsNotNone(self.dao)

#----------------------UF-----------------------------------
class TestUF(SimpleTestCase):
    """docstring for TestDAO"""
    def setUp(self):    #configura ambiente para teste
        self.uf = uf_dao.UfDAO()
        #descobre qual metodo será chamado e formata a saída
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_',' ')
        out = '\rTeste de ' + func + ' '
        print out.ljust(65,'-'),

    def tearDown(self):
        # informa que o teste foi realizado
        print 'Done'                       

    def shortDescription(self):
            print "Teste da classe GenericoDAO"

    def test_existing_uf_dao_instance(self):
        self.assertIsNotNone(self.uf)

    def test_list_uf(self):
        for i in self.uf.lista_ufs():
            self.assertIsNotNone(i)