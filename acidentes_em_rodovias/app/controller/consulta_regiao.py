# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import re
import MySQLdb
from django.utils.datastructures import MultiValueDictKeyError
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models.dao.uf_dao import *
from models.dao.municipio_dao import *
from models.dao.ocorrencia_basica_dao import *

def consulta_por_regiao(request):
    try:
        uf_dao = UfDAO()
        uf_list = uf_dao.lista_ufs()
    except (MySQLdb.Error, ResultadoConsultaNuloError), e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

    return render_to_response("regiao.html", {'uf_list' : uf_list}, context_instance=RequestContext(request))

def consulta_municipios_na_regiao(request):
    try:
        uf_id = request.GET['uf_id']
    except MultiValueDictKeyError, e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

    try:
        valida_caracteres(uf_id)
    except ParametroInseguroClienteError, e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))                

    try:
        municipio_dao = MunicipioDAO()
        municipio_list = municipio_dao.lista_municipios(uf_id)
    except (MySQLdb.Error, ResultadoConsultaNuloError), e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

    return render_to_response("municipio.html", {'municipio_list' : municipio_list}, context_instance=RequestContext(request))

def consulta_ocorrencias_por_municipio(request):
    try:
        municipio_id = int(request.GET['municipio_id'])
    except (ValueError, MultiValueDictKeyError), e:
        logger.error(str(e))
        erro = "Preencha corretamente o formulário!"
        return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))        

    try:
        ocorrencia_dao = OcorrenciaBasicaDAO()
        ocorrencia_list = ocorrencia_dao.lista_ocorrencias_por_regiao(municipio_id, 1000)
    except (MySQLdb.Error, ResultadoConsultaNuloError), e:
        logger.error(str(e))
        erro = "Ocorreu um erro no sistema, tente novamente mais tarde!"
        return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

    if (len(ocorrencia_list) == 0):
        erro = "A consulta não retornou resultados!"
        return render_to_response("index.html", {'erro' : erro}, context_instance=RequestContext(request))

    municipio = ocorrencia_list[0].tmudenominacao
    uf = ocorrencia_list[0].tmuuf

    return render_to_response("resultado.html", {'ocorrencia_list' : ocorrencia_list, 'tipo_consulta' : 'regiao', 'municipio' : municipio , 'uf' : uf}, context_instance=RequestContext(request))
