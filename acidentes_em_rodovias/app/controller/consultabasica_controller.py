# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from model.dao.uf_dao import *
from model.dao.municipio_dao import *
from model.dao.ocorrencia_basica_dao import *

def index(request):
	return render_to_response("index.html", context_instance=RequestContext(request))	

def consulta_por_regiao(request):
	uf_dao = UfDAO()
	uf_list = uf_dao.lista_ufs()
	
	return render_to_response("regiao.html", {'uf_list' : uf_list}, context_instance=RequestContext(request))

def consulta_municipios_na_regiao(request):
	uf_id = request.GET['uf_id']

	municipio_dao = MunicipioDAO()
	municipio_list = municipio_dao.lista_municipios(uf_id)

	return render_to_response("municipio.html", {'municipio_list' : municipio_list}, context_instance=RequestContext(request))

def consulta_ocorrencias_por_municipio(request):
	municipio_id = int(request.GET['municipio_id'])

	ocorrencia_dao = OcorrenciaBasicaDAO()
	ocorrencia_list = ocorrencia_dao.lista_ocorrencias_por_regiao(municipio_id, 1000)

	return render_to_response("resultado.html", {'ocorrencia_list' : ocorrencia_list, 'tipo_consulta' : 'regiao'}, context_instance=RequestContext(request))

def consulta_por_periodo(request):
    return render_to_response("periodo.html", context_instance=RequestContext(request))

def consulta_por_rodovia(request):
    return render_to_response("rodovia.html", context_instance=RequestContext(request))