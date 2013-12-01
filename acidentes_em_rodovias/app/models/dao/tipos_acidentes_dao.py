# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from models.tipos_acidentes import *
from util.estatisticas_util import *

class TiposAcidentesDAO(GenericoDAO):
	def tipos_acidentes(self):
		query = """SELECT tipo, SUM(quantidade_ocorrencias) AS quantidade_ocorrencias
				 FROM estatisticas_tipo
				 GROUP BY  tipo
				 ORDER BY quantidade_ocorrencias DESC; """

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "TiposAcidentes", "tipos_acidentes")

	def tipos_acidentes_ano(self):
		query = """SELECT tipo, quantidade_ocorrencias, ano
				 FROM estatisticas_tipo 
				 ORDER BY tipo, ano ; """
		
		resultado_query = self.executa_query(query)

		tipos_acidentes_ano_list = []
		ultimo_tipo = ''
		for (tipo, quantidade_ocorrencias, ano) in zip(resultado_query['tipo'].values(), resultado_query['quantidade_ocorrencias'].values(), resultado_query['ano'].values()):
			tipo = tipo.decode('iso-8859-1').encode('utf8')
			if (ultimo_tipo != tipo):
				tipos_acidentes_ano =  TiposAcidentesAno()
				tipos_acidentes_ano_list.append(tipos_acidentes_ano)
				tipos_acidentes_ano.tipo = tipo
				ultimo_tipo = tipo
			tipos_acidentes_ano.ano_list.append(ano)
			tipos_acidentes_ano.quantidade_ocorrencias_list.append(quantidade_ocorrencias)

		return tipos_acidentes_ano_list

	def probabilidade_tipos_acidentes(self):
		query = """SELECT tipo, quantidade_ocorrencias, ano
				 FROM estatisticas_tipo 
				 ORDER BY tipo, ano ; """
		
		data_frame = self.executa_query(query, get_data_frame=True)
		medias_list = data_frame.groupby('tipo')['quantidade_ocorrencias'].mean()
		desvios_padroes_list = data_frame.groupby('tipo')['quantidade_ocorrencias'].std()
		probabilidade_tipo_list = []
		
		for i in range(0, len(medias_list)):
			probabilidade_tipo = ProbabilidadeTiposAcidentes()
			probabilidade_tipo.tipo = medias_list.keys()[i].decode('iso-8859-1').encode('utf8')
			
			limites = [(0,1000), (1001,5000), (5001,10000), (10001,50000), (50001, sys.maxint)]
			for (inferior, superior) in limites:
				if (medias_list[i] >= inferior and medias_list[i] <= superior):
					probabilidade_tipo.probabilidade_por_limite_list.append(100 * (distribuicao_normal(inferior, medias_list[i], desvios_padroes_list[i]) + distribuicao_normal(superior, medias_list[i], desvios_padroes_list[i])))
				elif (medias_list[i] >= inferior):
					probabilidade_tipo.probabilidade_por_limite_list.append(100 * (distribuicao_normal(inferior, medias_list[i], desvios_padroes_list[i]) - distribuicao_normal(superior, medias_list[i], desvios_padroes_list[i])))
				elif (medias_list[i] <= inferior):
					probabilidade_tipo.probabilidade_por_limite_list.append(100 * (distribuicao_normal(superior, medias_list[i], desvios_padroes_list[i]) - distribuicao_normal(inferior, medias_list[i], desvios_padroes_list[i])))	
			
			probabilidade_tipo_list.append(probabilidade_tipo)

		return probabilidade_tipo_list
	
	def media_desvio_tipos_acidentes(self):
		query = """SELECT tipo, quantidade_ocorrencias, ano
				 FROM estatisticas_tipo 
				 ORDER BY tipo, ano ; """		
		
		data_frame = self.executa_query(query, get_data_frame=True)
		medias_list = data_frame.groupby('tipo')['quantidade_ocorrencias'].mean()
		desvios_padroes_list = data_frame.groupby('tipo')['quantidade_ocorrencias'].std()
		media_desvio_tipos_acidentes_list = []
		for i in range(0, len(medias_list)):
			media_desvio_tipos_acidentes = MediaDesvioTiposAcidentes()
			media_desvio_tipos_acidentes.media = medias_list[i]
			media_desvio_tipos_acidentes.desvio = desvios_padroes_list[i]

			media_desvio_tipos_acidentes_list.append(media_desvio_tipos_acidentes)

		return media_desvio_tipos_acidentes_list