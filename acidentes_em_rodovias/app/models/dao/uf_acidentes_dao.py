# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from models.uf_acidentes import *

coordenadas_capitais = {
	'AC' : (-9.976536213,-67.82207776),
	'AL' : (-9.6476843,-35.7339264),
	'AP' : (0.0456321,-51.0632732),
	'AM' : (-3.133105484,-59.9856354),
	'BA' : (-12.98163556,-38.48207707),
	'CE' : (-3.73045122,-38.52179892),
	'DF' : (-15.7941878,-47.8827491),
	'ES' : (-20.2833,-40.3078),
	'GO' : (-16.6801564,-49.2566208),
	'MA' : (-2.5319224, -44.2933276),
	'MT' : (-15.5992274,-56.0950526,),
	'MS' : (-20.4333215,-54.59458106),
	'MG' : (-19.9227318,-43.945094),
	'PR' : (-25.43564965,-49.2541945),
	'PB' : (-7.1178011,-34.8321878),
	'PA' : (-1.4672638, -48.30168268),
	'PE' : (-8.058107723,-34.89790466),
	'PI' : (-5.089640283,-42.809588),
	'RJ' : (-22.9112163,-43.2093781),
	'RN' : (-5.805397996,-35.20809053),
	'RS' : (-30.02094118,-51.21752276),
	'RR' : (2.49182134, -60.4034635),
	'RO' : (-8.748841665,-63.88682177),
	'SC' : (-27.5958016,-48.542915),
	'SE' : (-10.92332961,-37.08941953),
	'SP' : (-23.5561782,-46.6375468),
	'TO' : (-10.18855634,-48.33694214),
}

class UFAcidentesDAO(GenericoDAO):
	def acidentes_uf_geral(self):
		query = """SELECT ufe.uf, SUM(ufe.quantidade_ocorrencias) AS quantidade_ocorrencias
				FROM estatisticas_uf ufe
				GROUP BY ufe.uf
				ORDER BY quantidade_ocorrencias DESC;"""
		
		resultado_query = self.executa_query(query)

		uf_acidentes_list = []
		for (uf, quantidade_ocorrencias) in zip(resultado_query['uf'].values(), resultado_query['quantidade_ocorrencias'].values()):
			uf = uf.decode('iso-8859-1').encode('utf8')
			uf_acidentes =  UFAcidentes()
			uf_acidentes.uf = uf
			uf_acidentes.latitude = coordenadas_capitais[uf][0]
			uf_acidentes.longitude = coordenadas_capitais[uf][1]
			uf_acidentes.quantidade_ocorrencias = quantidade_ocorrencias

			uf_acidentes_list.append(uf_acidentes)

		return uf_acidentes_list

	def acidentes_uf_ano(self):
		query = """SELECT u.tufdenominacao AS uf, ufe.uf AS uf_sigla, ufe.quantidade_ocorrencias, ufe.ano
				FROM estatisticas_uf ufe
				INNER JOIN uf u
					ON u.tufuf = ufe.uf
				GROUP BY ufe.uf, ufe.ano
				ORDER BY ufe.uf;"""

		resultado_query = self.executa_query(query)

		uf_acidentes_ano_list = []
		ultima_uf = ''
		ufs_mais_acidentes = [i.uf for i in self.acidentes_uf_geral()[:10]]
		for (uf, uf_sigla, quantidade_ocorrencias, ano) in zip(resultado_query['uf'].values(), resultado_query['uf_sigla'].values(), resultado_query['quantidade_ocorrencias'].values(), resultado_query['ano'].values()):
			uf = uf.decode('iso-8859-1').encode('utf8')
			if (uf_sigla in ufs_mais_acidentes) is False:
				continue

			if (ultima_uf != uf):
				ufs_acidentes_ano =  UFAcidentesAno()
				uf_acidentes_ano_list.append(ufs_acidentes_ano)
				ufs_acidentes_ano.uf = uf
				ultima_uf = uf
			ufs_acidentes_ano.ano_list.append(ano)
			ufs_acidentes_ano.quantidade_ocorrencias_list.append(quantidade_ocorrencias)

		return uf_acidentes_ano_list