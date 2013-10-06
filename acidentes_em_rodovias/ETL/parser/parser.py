#!/usr/bin/python
#-*- encoding: utf-8 -*-

try:
	import sys	#carregar ambiente do sistema
	from pandas import *  #Suporte para bd oriundo do csv
	import matplotlib.pyplot as plt	#caso deseje plotar algo
	import urllib2	#acessar site
	from BeautifulSoup import BeautifulSoup #filtrar links desejados
except ImportError , ex:
	print ex
	print "try:\n sudo pip install " +  str(ex).split(' ')[-1]
	quit()

def update():
	'''
	TODO: 
		Inserir verificação de novos arquivos.
		Inserir validação de url final
		Inserir wget dos arquivos para diretório pré-definido
		
	'''
	
	url='http://repositorio.dados.gov.br/transportes-transito/transito/'
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content)
	files=[] 
	for links in soup.findAll('a'):
		#seleciona *.zip
		if '.zip' in links.get('href'):
			files.append(str( links.get('href')))
		#se houver algum csv solto, seleciona também
		if '.csv' in links.get('href'):
			files.append(str( links.get('href')))

	#imprimindo *.zip e *.csv disponíveis para download
	for i in files:
		print url+ i


if __name__ == "__main__":
	from pandas.tools.plotting import andrews_curves
	from pandas.tools.plotting import lag_plot

	if(len(sys.argv)>1):
		filename = sys.argv[1]
	else:
		filename = "estadofisico.csv"

	print "Arquivos disponíveis pra baixar:"
	update()

	"""
	'''Fazendo de uso da pandas'''
	#Fazendo leitura de CSV, codificação em utf-8
	DataFrame = read_csv(filename,delimiter = ';', na_values=["(null)"],encoding='utf-8') 
	# Recomendo alterar a largura do terminal para conseguir ver essa informação corretamente
	print DataFrame.describe()
	#imprimindo variância dos dados
	print 'var' + str(list(DataFrame.var())[0]).rjust(12)

	'''
	DataFrame.count().plot(kind='bar')
	plt.hold()
	DataFrame.count().plot(kind='kde')
	plt.show()
	#TODO: Este campo esta vazio ou é minha impressão???
	print DataFrame['pespaiscnh']
	
	DataFrame = read_csv("pessoa_2_Semestre_2012.csv",delimiter = ';', na_values=["(null)"])  
	#imprimindo variância dos dados
	print DataFrame.var()
	# Plotando dados
	#DataFrame['pesidade'][:50].plot(kind='bar') #apenas os 50 primeiros dados
	DataFrame.std().plot(kind='kde')
	
	andrews_curves(DataFrame, 'estadofisico')
	plt.show() #Forçar amostrar da imagem
		
	
	#imprimindo DataFrame
	print DataFrame
	
	#imprimindo chaves do DataFrame
	print DataFrame.keys()
	
	#convertendo para dicionario
	Pessoa = DataFrame.to_dict()
	print "Quantidade de colunas: ",
	print len(Pessoa.keys())

	#Utilizando as chaves do dict para selecionar informação desejada
	print DataFrame[Pessoa.keys()[0]]

	#summary statistics de uma coluna em especifico
	print DataFrame['peslesao'].describe()
	
	#imprime a média de todos os objetos
	print DataFrame.mean()
	

	DataFrame = read_csv(filename,delimiter = ';', na_values=["(null)"])  
	#convertendo para HTML
	Pessoa_html = DataFrame.to_html()
	f = open('workfile.html', 'w')
	f.write(Pessoa_html)
	'''
	"""
	
	
