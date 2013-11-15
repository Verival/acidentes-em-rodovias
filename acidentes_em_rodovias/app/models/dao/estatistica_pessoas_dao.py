# -*- coding: utf-8 -*-

from generico_dao import *

class EstatisticaPessoasDAO(GenericoDAO):
	#def acidentes_por_sexo_e_ano(self, ano):
	#	query = """SELECT p.pessexo, COUNT(*) AS 'quantidade'
	#			FROM ocorrencia AS o
	#			INNER JOIN ocorrenciaPessoa AS op ON op.opeocoid = o.ocoid
	#			INNER JOIN pessoa AS p ON p.pesid = op.opepesid
	#			WHERE o.ano = %d AND p.pessexo IS NOT NULL
	#			GROUP BY p.pessexo
	#			ORDER BY COUNT( * ) DESC 
	#			LIMIT 0 , 30;""" % (ano)

	#	return self.transforma_dicionario_em_objetos(self.executa_query(query), "EstatisticaPessoas", "estatistica_pessoas")

	def acidentes_por_sexo(self, sexo):
		query = """SELECT a.ano, a.sexo, a.quantidade 
				FROM acidentes_por_sexo AS a
				WHERE a.sexo = '%s'
				ORDER BY a.ano;""" % (sexo)

		return self.transforma_dicionario_em_objetos(self.executa_query(query), "EstatisticaPessoas", "estatistica_pessoas")

#if __name__ == '__main__':
#	dao = EstatisticaPessoasDAO()
#	teste = dao.acidentes_por_sexo('M')
#
#	for i in teste:
#		print i
