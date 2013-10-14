# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
import dao

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
	
	elif (tipo_consulta == "regiao"):
		cidade = request.GET['cidade']
		uf = request.GET['uf']

		print cidade
		print uf
	
	return render_to_response("resultado.html", {}, context_instance=RequestContext(request))