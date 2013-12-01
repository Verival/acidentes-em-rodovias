# -*- coding: utf-8 -*-

from generico_dao import *

class PessoasAcidentesDAO(GenericoDAO):
	def acidentes_por_sexo_e_ano(self, sexo):
		query = """SELECT a.ano, a.sexo, a.quantidade 
				FROM acidentes_por_sexo AS a
				WHERE a.sexo = '%s'
				ORDER BY a.ano;""" % (sexo)

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "PessoasAcidentes", "pessoas_acidentes")

	def acidentes_por_sexo_geral(self, sexo):
		query = """SELECT a.sexo, SUM(a.quantidade) AS quantidade
				FROM acidentes_por_sexo AS a
				WHERE a.sexo = '%s'
				ORDER BY a.ano;""" % (sexo)

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "PessoasAcidentesGeral", "pessoas_acidentes")