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
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

from models.dao.estatistica_pessoas_dao import *

def tipos_causas(request):
	return render_to_response("tipos_causas.html", context_instance=RequestContext(request))

def acidentes_sexo(request):
	estatistica_dao = EstatisticaPessoasDAO()
	homens = estatistica_dao.acidentes_por_sexo('M')
	mulheres = estatistica_dao.acidentes_por_sexo('F')

	return render_to_response("acidentes_sexo.html",{'homens':homens, 'mulheres':mulheres}, context_instance=RequestContext(request))