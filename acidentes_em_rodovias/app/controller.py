# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from dao import *

def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))
   
def consulta_por_regiao(request):
	cidades_dao = DAO("municipio")
	cidade_list = cidades_dao.consulta_todos(1000)
	return render_to_response("regiao.html", {'cidade_list' : cidade_list}, context_instance=RequestContext(request))

def consulta_por_periodo(request):
    return render_to_response("periodo.html", context_instance=RequestContext(request))

def consulta_por_pessoa(request):
    return render_to_response("pessoa.html", context_instance=RequestContext(request))

def consulta_por_rodovia(request):
    return render_to_response("rodovia.html", context_instance=RequestContext(request))
   
def executa_consulta(request, tipo_consulta):
	dao = OcorrenciaResultadosDAO()
	ocorrencia_resultados_list = []
	dados_especificos = {}
	erros = []

	if (tipo_consulta == "periodo"):
		try:
			data_de = request.GET['data_de']
			data_ate = request.GET['data_ate']
		except Exception, ex:
			erros.append("Os campos de consulta não podem ser nulos, tente novamente!")
			return render_to_response("resultado.html", {'resultados_list' : ocorrencia_resultados_list, 'tipo_consulta' : tipo_consulta, 'dados_especificos' : dados_especificos, 'erros' : erros}, context_instance=RequestContext(request))

		print data_de
		print data_ate
	elif (tipo_consulta == "pessoa"):
		try:
			nome_envolvido = request.GET['nome_envolvido']
		except Exception, ex:
			erros.append("Os campos de consulta não podem ser nulos, tente novamente!")
			return render_to_response("resultado.html", {'resultados_list' : ocorrencia_resultados_list, 'tipo_consulta' : tipo_consulta, 'dados_especificos' : dados_especificos, 'erros' : erros}, context_instance=RequestContext(request))

		print nome_envolvido
	elif (tipo_consulta == "regiao"):
		try:
			cidade = int(request.GET['cidade'])
		except Exception, ex:
			erros.append("Os campos de consulta não podem ser nulos, tente novamente!")
			return render_to_response("resultado.html", {'resultados_list' : ocorrencia_resultados_list, 'tipo_consulta' : tipo_consulta, 'dados_especificos' : dados_especificos, 'erros' : erros}, context_instance=RequestContext(request))

		try:
			ocorrencia_resultados_list = dao.consulta_por_municipio(cidade, 100)
		except Exception, ex:
			erros.append("Erro no sistema, tente novamente mais tarde!")
			return render_to_response("resultado.html", {'resultados_list' : ocorrencia_resultados_list, 'tipo_consulta' : tipo_consulta, 'dados_especificos' : dados_especificos, 'erros' : erros}, context_instance=RequestContext(request))			
		
		try:
			nome_cidade = ocorrencia_resultados_list[0].tmudenominacao
			nome_uf = ocorrencia_resultados_list[0].tmuuf
			dados_especificos = {'cidade' : nome_cidade, 'uf' : nome_uf}
		except Exception, ex:
			erros.append("A consulta não retornou resultados, tente novamente com uma consulta diferente!")
			return render_to_response("resultado.html", {'resultados_list' : ocorrencia_resultados_list, 'tipo_consulta' : tipo_consulta, 'dados_especificos' : dados_especificos, 'erros' : erros}, context_instance=RequestContext(request))			

	# Sucesso!
	return render_to_response("resultado.html", {'resultados_list' : ocorrencia_resultados_list, 'tipo_consulta' : tipo_consulta, 'dados_especificos' : dados_especificos}, context_instance=RequestContext(request))