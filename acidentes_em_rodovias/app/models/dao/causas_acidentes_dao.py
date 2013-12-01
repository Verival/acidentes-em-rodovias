# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from models.causas_acidentes import *
from util.estatisticas_util import *

class CausasAcidentesDAO(GenericoDAO):
	def causas_acidentes(self):
		query = """SELECT causa, SUM(quantidade_ocorrencias) AS quantidade_ocorrencias
				 FROM estatisticas_causa
				 GROUP BY  causa
				 ORDER BY quantidade_ocorrencias DESC; """

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "CausasAcidentes", "causas_acidentes")

	def causas_acidentes_ano(self):
		query = """SELECT causa, quantidade_ocorrencias, ano
				 FROM estatisticas_causa 
				 ORDER BY causa, ano ; """
		
		resultado_query = self.executa_query(query)

		causas_acidentes_ano_list = []
		ultimo_causa = ''
		for (causa, quantidade_ocorrencias, ano) in zip(resultado_query['causa'].values(), resultado_query['quantidade_ocorrencias'].values(), resultado_query['ano'].values()):
			causa = causa.decode('iso-8859-1').encode('utf8')
			if (ultimo_causa != causa):
				causas_acidentes_ano =  CausasAcidentesAno()
				causas_acidentes_ano_list.append(causas_acidentes_ano)
				causas_acidentes_ano.causa = causa
				ultimo_causa = causa
			causas_acidentes_ano.ano_list.append(ano)
			causas_acidentes_ano.quantidade_ocorrencias_list.append(quantidade_ocorrencias)

		return causas_acidentes_ano_list

	def probabilidade_causas_acidentes(self):
		query = """SELECT causa, quantidade_ocorrencias, ano
				 FROM estatisticas_causa 
				 ORDER BY causa, ano ; """
		
		data_frame = self.executa_query(query, get_data_frame=True)
		medias_list = data_frame.groupby('causa')['quantidade_ocorrencias'].mean()
		desvios_padroes_list = data_frame.groupby('causa')['quantidade_ocorrencias'].std()
		probabilidade_causas_acidentes_list = []
		
		for i in range(0, len(medias_list)):
			probabilidade_causas_acidentes = ProbabilidadeCausasAcidentes()
			probabilidade_causas_acidentes.causa = medias_list.keys()[i].decode('iso-8859-1').encode('utf8')
			
			limites = [(0,5000), (5001,10000), (10001,30000), (30001,50000), (50001, sys.maxint)]
			for (inferior, superior) in limites:
				if (medias_list[i] >= inferior and medias_list[i] <= superior):
					probabilidade_causas_acidentes.probabilidade_por_limite_list.append(100 * (distribuicao_normal(inferior, medias_list[i], desvios_padroes_list[i]) + distribuicao_normal(superior, medias_list[i], desvios_padroes_list[i])))
				elif (medias_list[i] >= inferior):
					probabilidade_causas_acidentes.probabilidade_por_limite_list.append(100 * (distribuicao_normal(inferior, medias_list[i], desvios_padroes_list[i]) - distribuicao_normal(superior, medias_list[i], desvios_padroes_list[i])))
				elif (medias_list[i] <= inferior):
					probabilidade_causas_acidentes.probabilidade_por_limite_list.append(100 * (distribuicao_normal(superior, medias_list[i], desvios_padroes_list[i]) - distribuicao_normal(inferior, medias_list[i], desvios_padroes_list[i])))	
			
			probabilidade_causas_acidentes_list.append(probabilidade_causas_acidentes)

		return probabilidade_causas_acidentes_list
	
	def media_desvio_causas_acidentes(self):
		query = """SELECT causa, quantidade_ocorrencias, ano
				 FROM estatisticas_causa 
				 ORDER BY causa, ano ; """		
		
		data_frame = self.executa_query(query, get_data_frame=True)
		medias_list = data_frame.groupby('causa')['quantidade_ocorrencias'].mean()
		desvios_padroes_list = data_frame.groupby('causa')['quantidade_ocorrencias'].std()
		media_desvio_causas_acidentes_list = []
		for i in range(0, len(medias_list)):
			media_desvio_causas_acidentes = MediaDesvioCausasAcidentes()
			media_desvio_causas_acidentes.media = medias_list[i]
			media_desvio_causas_acidentes.desvio = desvios_padroes_list[i]

			media_desvio_causas_acidentes_list.append(media_desvio_causas_acidentes)

		return media_desvio_causas_acidentes_list