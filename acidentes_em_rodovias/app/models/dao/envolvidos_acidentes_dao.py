# -*- coding: utf-8 -*-
from generico_dao import GenericoDAO
import sys, os, inspect
current_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(current_path)
current_path = os.path.dirname(os.path.abspath('.'))
sys.path.append(current_path)

from models.envolvidos_acidentes import *
from util.estatisticas_util import *

class EnvolvidosAcidentesDAO(GenericoDAO):
	def envolvidos_acidentes(self):
		query = """SELECT `quantidade_envolvidos`, `quantidade_acidentes`, `ano`
				FROM `estatisticas_envolvido`;"""

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "EnvolvidosAcidente", "envolvidos_acidentes")

	def media_desvio_envolvidos(self):
		lista_envolvidos = self.envolvidos_acidentes()

		lista_medias = []
		for envolvido in lista_envolvidos:
			envolvidos = float(envolvido.quantidade_envolvidos)
			acidentes = float(envolvido.quantidade_acidentes)
			media = envolvidos/acidentes
			lista_medias.append(media)

		desvio = desvio_padrao(lista_medias)

		return lista_medias, desvio
		

if __name__ == '__main__':
	dao = EnvolvidosAcidentesDAO()
	print dao.media_desvio_envolvidos()