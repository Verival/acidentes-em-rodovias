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
from models.dao.uf_acidentes_dao import *
from datetime import datetime
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

def acidentes_uf(request):
	try:
		data = datetime.now()
		uf_dao = UFAcidentesDAO()
		uf_acidentes_geral = uf_dao.acidentes_uf_geral()
		uf_acidentes_ano = uf_dao.acidentes_uf_ano()

	except (MySQLdb.Error, ResultadoConsultaNuloError), e:
		logger.error(str(e))
		erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
		return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

	return  render_to_response("uf_acidentes.html",{'ano':range(2007, data.year+1),'uf_acidentes_ano':uf_acidentes_ano, 
		'uf_acidentes_geral':uf_acidentes_geral[:10],
		'uf_acidentes_geral_mapa':uf_acidentes_geral
		}, context_instance=RequestContext(request))