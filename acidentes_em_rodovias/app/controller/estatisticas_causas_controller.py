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
from models.dao.causas_acidentes_dao import *
from datetime import datetime
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

def causas_acidentes(request):
	try:
		causas_acidentes_dao = CausasAcidentesDAO()
		causas_acidentes_list = causas_acidentes_dao.causas_acidentes()
		causas_acidentes_ano_list = causas_acidentes_dao.causas_acidentes_ano()
		probabilidade_causas_acidentes_list = causas_acidentes_dao.probabilidade_causas_acidentes()
		media_desvio_causas_acidentes_list = causas_acidentes_dao.media_desvio_causas_acidentes()
	except (MySQLdb.Error, ResultadoConsultaNuloError), e:
		logger.error(str(e))
		erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
		return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

	return render_to_response("causas_acidentes.html",{
		'causas_acidentes_list' : causas_acidentes_list, 
		'causas_acidentes_ano_list' : causas_acidentes_ano_list,
		'anos' : causas_acidentes_ano_list[0].ano_list,
		'probabilidade_causas_acidentes_list' : probabilidade_causas_acidentes_list,
		'causas' : [i.causa for i in probabilidade_causas_acidentes_list], 
		'media_desvio_causas_acidentes_list' : media_desvio_causas_acidentes_list,
		}, context_instance=RequestContext(request))	
	return render_to_response("causas.html", context_instance=RequestContext(request))	
