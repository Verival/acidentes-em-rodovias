# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import MySQLdb
from django.utils.datastructures import MultiValueDictKeyError
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models.dao.ocorrencia_basica_dao import *
from exception.validation_exceptions import *
from exception.internal_exceptions import *
from util.validacao_util import *
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

def consulta_por_periodo(request):
	return render_to_response("periodo.html", context_instance=RequestContext(request))

def consulta_ocorrencias_por_periodo(request):
	try:
		data_inicio = str(request.GET['data_inicio'])
		data_fim = str(request.GET['data_fim'])
	except (MultiValueDictKeyError), e:
		logger.error(str(e))
		erro = "Preencha corretamente o formulário!"
		return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))		

	try:
		valida_data(data_inicio) 
		valida_data(data_fim)
	except DataInvalidaError, e:
		logger.error(str(e))
		erro = "Preencha corretamente o formulário!"
		return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))				
	
	try:
		ocorrencia_dao = OcorrenciaBasicaDAO()
		ocorrencia_list = ocorrencia_dao.lista_ocorrencias_por_periodo(data_inicio, data_fim, 1000)
	except (MySQLdb.Error, ResultadoConsultaNuloError), e:
		logger.error(str(e))
		erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
		return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

	return render_to_response("resultado.html", {'ocorrencia_list' : ocorrencia_list, 'tipo_consulta' : 'periodo', 'data_inicio' : data_inicio, 'data_fim' : data_fim}, context_instance=RequestContext(request))