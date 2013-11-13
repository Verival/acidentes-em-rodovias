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