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
from models.dao.uf_dao import *
from models.dao.municipio_dao import *
from models.dao.ocorrencia_basica_dao import *
from exception.validation_exceptions import *
from exception.internal_exceptions import *
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)

def index(request):
	return render_to_response("index.html", context_instance=RequestContext(request))	