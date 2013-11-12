# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from models.ocorrencias_tipo import *
from util.estatisticas_util import *

class TiposDAO(GenericoDAO):
	def ocorrencias_tipo(self):
		query = """SELECT ta.ttadescricao, COUNT(*) AS 'quantidade_ocorrencias'
				 FROM ocorrencia AS o 
				 INNER JOIN ocorrenciaacidente AS oa ON o.ocoid = oa.oacocoid 
				 INNER JOIN tipoAcidente AS ta ON oa.oacttacodigo = ta.ttacodigo 
				 GROUP BY ta.ttadescricao 
				 ORDER BY COUNT(*) DESC; """

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "OcorrenciasTipo", "ocorrencias_tipo")

	def ocorrencias_tipo_ano(self):
		query = """SELECT ta.ttadescricao, COUNT(*) AS  'quantidade_ocorrencias', o.ano
				FROM ocorrencia AS o
				INNER JOIN ocorrenciaacidente AS oa ON o.ocoid = oa.oacocoid
				INNER JOIN tipoAcidente AS ta ON oa.oacttacodigo = ta.ttacodigo
				GROUP BY ta.ttadescricao, o.ano
				ORDER BY ta.ttadescricao, o.ano """
		
		resultado_query = self.executa_query(query)

		ocorrencias_tipo_ano_list = []
		ultimo_tipo = ''
		for (tipo, quantidade, ano) in zip(resultado_query['ttadescricao'].values(), resultado_query['quantidade_ocorrencias'].values(), resultado_query['ano'].values()):
			tipo = tipo.decode('iso-8859-1').encode('utf8')
			if (ultimo_tipo != tipo):
				ocorrencias_tipo_ano =  OcorrenciasTipoAno()
				ocorrencias_tipo_ano_list.append(ocorrencias_tipo_ano)
				ocorrencias_tipo_ano.ttadescricao = tipo
				ultimo_tipo = tipo
			ocorrencias_tipo_ano.ano_list.append(ano)
			ocorrencias_tipo_ano.quantidade_ocorrencias_list.append(quantidade)

		return ocorrencias_tipo_ano_list

	def probabilidade_ocorrencias_tipo(self):
		query = """SELECT ta.ttadescricao, COUNT(*) AS  'quantidade_ocorrencias', o.ano
				FROM ocorrencia AS o
				INNER JOIN ocorrenciaacidente AS oa ON o.ocoid = oa.oacocoid
				INNER JOIN tipoAcidente AS ta ON oa.oacttacodigo = ta.ttacodigo
				GROUP BY ta.ttadescricao, o.ano
				ORDER BY ta.ttadescricao, o.ano """		
		
		data_frame = self.executa_query(query, get_data_frame=True)
		medias_list = data_frame.groupby('ttadescricao')['quantidade_ocorrencias'].mean()
		desvios_padroes_list = data_frame.groupby('ttadescricao')['quantidade_ocorrencias'].std()
		probabilidade_tipo_list = []
		
		for i in range(0, len(medias_list)):
			probabilidade_tipo = ProbabilidadeTipo()
			probabilidade_tipo.ttadescricao = medias_list.keys()[i].decode('iso-8859-1').encode('utf8')
			
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
			