# -*- coding: utf-8 -*-
import sys
from dao.ufDAO import *

class Uf:
	def __init__(self):
		self.id = ''
		self.data_ocorrencia = ''
		self.data_registro = ''
		self.veiculo_envolvido = ''
		self.tipo = ''
		self.municipio = ''
		self.uf = ''
		self.unidade_operacional = ''
		self.tipo_unidade_operacional = ''
		self.endereco_unidade_operacional = ''

	def transforma_em_objeto(self, resultado_query):
		lista_uf = []

		for registro in range(0, len(resultado_query)):
			uf = Uf()
			coluna = 0
			for atributo in uf.__dict__:
				setattr(uf, atributo, resultado_query[registro][coluna])
				coluna = coluna + 1
			lista_uf.append(uf)

		return lista_uf

	def consultar_banco(self,uf):
		if(len(sys.argv)>1):
			dao = UfDAO(sys.argv[1])
		else:
			dao = UfDAO()
		resultado_query = dao.listar_ocorrencias(uf, 5)
		print resultado_query

		return  self.transforma_em_objeto(resultado_query)

	def __str__(self):
		return str(self.__dict__)


if __name__ == '__main__':
	uf = Uf()
	
	for i in uf.consultar_banco('DF'):
		print i
