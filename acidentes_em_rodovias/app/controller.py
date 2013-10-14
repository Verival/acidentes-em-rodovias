# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):

    return render_to_response("index.html", context_instance=RequestContext(request))
   
def consulta_por_regiao(request):

    return render_to_response("regiao.html", context_instance=RequestContext(request))

def consulta_por_periodo(request):

    return render_to_response("periodo.html", context_instance=RequestContext(request))

def consulta_por_pessoa(request):

    return render_to_response("pessoa.html", context_instance=RequestContext(request))

def consulta_por_rodovia(request):

    return render_to_response("rodovia.html", context_instance=RequestContext(request))
   
def executa_consulta(request, tipo_consulta):
	
	if (tipo_consulta == "periodo"):
		data_de = request.GET['data_de']
		print data_de
		data_ate = request.GET['data_ate']
		print data_ate
		
	elif (tipo_consulta == "pessoa"):
		nome_envolvido = request.GET['nome_envolvido']
		print nome_envolvido
		
		# Tem que pesquisar pessoas com o nome = nome_envolvido
		dao = DAO('pessoa')
		for i in dao.consulta_todos(3):
			print i
			dao.troca_tabela("pessoa")
		for i in dao.consulta_todos(3):
			print i
	
	return render_to_response("resultado.html", {}, context_instance=RequestContext(request))