# -*- coding: utf-8 -*-

from dao.municipioDAO import *

class Municipio:
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
		lista_municipio = []

		for registro in range(0, len(resultado_query)):
			municipio = Municipio()
			coluna = 0
			for atributo in municipio.__dict__:
				setattr(municipio, atributo, resultado_query[registro][coluna])
				coluna = coluna + 1
			lista_municipio.append(municipio)

		return lista_municipio

	def consultar_banco(self, municipio):
		if(len(sys.argv)>1):
			municipioDAO = MunicipioDAO(sys.argv[1])
		else:
			municipioDAO = MunicipioDAO()

		resultado_query = municipioDAO.listar_ocorrencias(municipio, 5)

		return  self.transforma_em_objeto(resultado_query)

	def __str__(self):
		return str(self.__dict__)


if __name__ == '__main__':
	municipio = Municipio()
	
	for i in municipio.consultar_banco(35):
		print i
