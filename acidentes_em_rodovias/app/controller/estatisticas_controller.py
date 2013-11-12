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
from exception.validation_exceptions import *
from exception.internal_exceptions import *
from models.dao.tipos_dao import *
from models.dao.estatistica_pessoas_dao import *
from itertools import groupby
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

def tipos_ocorrencia(request):
	try:
		tipos_dao = TiposDAO()
		ocorrencias_tipo_list = tipos_dao.ocorrencias_tipo()
		ocorrencias_tipo_ano_list = tipos_dao.ocorrencias_tipo_ano()
		probabilidade_ocorrencias_tipo_list = tipos_dao.probabilidade_ocorrencias_tipo()
	except (MySQLdb.Error, NoPandasComponentError), e:
		logger.error(str(e))
		erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
		return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

	return render_to_response("tipos.html",{
		'ocorrencias_tipo_list' : ocorrencias_tipo_list, 
		'ocorrencias_tipo_ano_list' : ocorrencias_tipo_ano_list,
		'anos' : ocorrencias_tipo_ano_list[0].ano_list,
		'probabilidade_ocorrencias_tipo_list' : probabilidade_ocorrencias_tipo_list,
		'tipos' : [i.ttadescricao for i in probabilidade_ocorrencias_tipo_list], 
		}, context_instance=RequestContext(request))	

def causas_ocorrencia(request):
	return render_to_response("causas.html", context_instance=RequestContext(request))	

def total_ocorrencias_envolvidos(request):
	return render_to_response("total-ocorrencias-envolvidos.html", context_instance=RequestContext(request))	

def acidentes_sexo(request):
	try:
		estatistica_dao = EstatisticaPessoasDAO()
		homens = estatistica_dao.acidentes_por_sexo('M')
		mulheres = estatistica_dao.acidentes_por_sexo('F')
	except (MySQLdb.Error, NoPandasComponentError), e:
		logger.error(str(e))
		erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
		return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

	return render_to_response("acidentes_sexo.html",{'homens':homens, 'mulheres':mulheres}, context_instance=RequestContext(request))