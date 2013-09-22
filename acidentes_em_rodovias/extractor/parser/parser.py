#!/usr/bin/python
#-*- encoding: utf-8 -*-

try:
	import csv, sys
	import odict
	from pandas import *  
	import matplotlib.pyplot as plt
except ImportError , ex:
	print ex
	print "try:\n sudo pip install " +  str(ex).split(' ')[-1]
	quit()
	
class parser(object):
	data={}
	"""
	@package Parser
	construtor das informações adquiridas através do arquivo CSV.
	
	"""
	def __init__(self,filename):
		with open(filename, 'rb') as filename:
			reader = csv.reader(filename, delimiter = ';', quotechar = '\"')
			try:
				self.data=odict.odict()
				for i in reader.next():
					self.data[str(i)] = []
				for row in reader:
					for (i,d) in zip(xrange(len(row)),self.data.keys()):
						self.data[d].append(row[i])
			except csv.Error as e:
				sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
			
			self.data=dict(self.data)
			

if __name__ == "__main__":
	'''Fazendo de uso da classe parser'''
	filename = "estadofisico.csv"
	estado_fisico=parser(filename)
	print estado_fisico.data

	'''Fazendo de uso da pandas'''
	#Fazendo leitura de CSV
	experimentDF = read_csv("pessoa_2_Semestre_2012.csv",delimiter = ';', na_values=["(null)"])  

	# Plotando dados
	experimentDF['pesidade'][:50].plot() #apenas os 50 primeiros dados
	plt.show() #Forçar amostrar da imagem
		
	'''
	#imprimindo DataFrame
	print experimentDF
	
	#imprimindo chaves do DataFrame
	print experimentDF.keys()
	
	#convertendo para dicionario
	Pessoa = experimentDF.to_dict()
	print "Quantidade de colunas: ",
	print len(Pessoa.keys())

	#Utilizando as chaves do dict para selecionar informação desejada
	print experimentDF[Pessoa.keys()[0]]

	#summary statistics de uma coluna em especifico
	print experimentDF['peslesao'].describe()
	
	#imprime a média de todos os objetos
	print experimentDF.mean()

	experimentDF = read_csv(filename,delimiter = ';', na_values=["(null)"])  
	#convertendo para HTML
	Pessoa_html = experimentDF.to_html()
	f = open('workfile.html', 'w')
	f.write(Pessoa_html)
	'''
	
	
	
