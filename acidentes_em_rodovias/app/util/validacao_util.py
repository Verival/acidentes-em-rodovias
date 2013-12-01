# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import re
from exception.validation_exceptions import *
from exception.internal_exceptions import *

def valida_data(data):
	if (re.search('^[0-3]\d/[01]\d/\d{4}$', data) is None 
		or int(data[0:2]) >= 32
		or int(data[3:5]) >= 13):
		raise DataInvalidaError("Data invalida inserida: " + data)

def valida_caracteres(palavra):
	if (re.search('^[\w\s]+$', str(palavra)) is None):
		raise ParametroInseguroClienteError("Parametro invalido inserido: " + palavra)
	if(palavra == None):
		raise ParametroInseguroClienteError("Parametro invalido inserido: enviado NONE" )