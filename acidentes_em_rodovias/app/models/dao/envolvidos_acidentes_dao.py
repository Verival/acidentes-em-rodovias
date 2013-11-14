# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from models.envolvidos_acidentes import *

class EnvolvidosAcidentesDAO(GenericoDAO):
	def envolvidos_acidentes(self):
		query = """SELECT `quantidade_envolvidos`, `quantidade_acidentes`, `ano`
				FROM `estatisticas_envolvido`;"""

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "EnvolvidosAcidente", "envolvidos_acidentes")