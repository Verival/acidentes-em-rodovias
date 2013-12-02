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
from models.dao.envolvidos_acidentes_dao import *
from models.dao.pessoas_acidentes_dao import *
from datetime import datetime
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)

def ocorrencias_e_envolvidos(request):
	envolvidosDAO = EnvolvidosAcidentesDAO()
	lista_envolvidos = envolvidosDAO.envolvidos_acidentes()
	medias, desvio = envolvidosDAO.media_desvio_envolvidos()
	anos = [i.ano for i in lista_envolvidos]

	ano_media_list = zip(anos, medias)

	return render_to_response("ocorrencias-e-envolvidos.html",{'lista_envolvidos':lista_envolvidos, 'ano_media_list':ano_media_list, 'desvio':desvio}, context_instance=RequestContext(request))	

def acidentes_sexo(request):
	try:
		pessoas_dao = PessoasAcidentesDAO()
		homens_ano = pessoas_dao.acidentes_por_sexo_e_ano('M')
		mulheres_ano = pessoas_dao.acidentes_por_sexo_e_ano('F')
		homens_geral = pessoas_dao.acidentes_por_sexo_geral('M')
		mulheres_geral = pessoas_dao.acidentes_por_sexo_geral('F')
		homens_geral, mulheres_geral = media_sexo(homens_geral, mulheres_geral)

	except (MySQLdb.Error, ResultadoConsultaNuloError), e:
		logger.error(str(e))
		erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
		return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

	return render_to_response("acidentes_sexo.html",{'homens_geral':homens_geral, 'mulheres_geral':mulheres_geral, 'homens_ano':homens_ano, 'mulheres_ano':mulheres_ano}, context_instance=RequestContext(request))
