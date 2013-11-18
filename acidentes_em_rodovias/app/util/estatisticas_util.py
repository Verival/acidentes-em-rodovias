import pandas
import os

prev_path = os.path.dirname(os.path.abspath(__file__))
arquivo_csv = open(prev_path + "/../resources/tabela-normal-reduzida.csv", "rb")
tabela = []
for linha in arquivo_csv:
	l = [float(i.strip()) for i in linha.split(';')]
	tabela.append(l)

def distribuicao_normal(x, media, desvio):
	z = (x-media)/float(abs(desvio))
	z = abs(int(z * 100) / 100.0)
	eixo_vertical = int(z * 10)	
	eixo_horizontal = int(z * 100) - 10*eixo_vertical
	try:
		p = tabela[eixo_vertical][eixo_horizontal]
	except IndexError, e:
		p = 0.5

	return p

def desvio_padrao(lista):
	media_total = 0
	for i in range(0,len(lista)):
		media_total = media_total + lista[i]
	media_total = media_total/len(lista)
	
	for i in range(0,len(lista)):
		desvio = (i - media_total)**2

	return (desvio/len(lista))**(0.5)

def media_sexo(homens, mulheres):
	total  = int(homens[0].quantidade) + int(mulheres[0].quantidade)
	for homem in homens:
		homem.quantidade = float(homem.quantidade)/float(total) * 100
	for mulher in mulheres:
		mulher.quantidade = float(mulher.quantidade)/float(total) * 100

	return homens[0], mulheres[0]
