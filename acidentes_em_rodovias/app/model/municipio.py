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

	def consultar_banco(self):
		dao = MunicipioDAO()
		resultado_query = dao.listar_ocorrencias()

		return  self.transforma_em_objeto(resultado_query)

	def imprimir_lista(self, lista_municipio):
		for i in lista_municipio:
			print 'ID: ', i.id
			print 'DATA DA OCORRENCIA: ', i.data_ocorrencia
			print 'DATA DA REGISTRO: ', i.data_registro
			print 'VEÍCULO ENVOLVIDO: ', i.veiculo_envolvido
			print 'TIPO DA OCORRENCIA: ', i.tipo
			print 'MUNICIPIO: ', i.municipio
			print 'UF:', i.uf
			print 'UNIDADE OPERACIONAL: ', i.unidade_operacional
			print 'TIPO UNIDADE OPERACIONAL:', i.tipo_unidade_operacional
			print 'ENDEREÇO: ', i.endereco_unidade_operacional
			print '\n'


if __name__ == '__main__':
	municipio = Municipio()
	
	municipio.imprimir_lista(municipio.consultar_banco())