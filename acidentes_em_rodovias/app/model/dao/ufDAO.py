# -*- coding: utf-8 -*-
import sys
from dao import DAO

class UfDAO(DAO):
	def listar_ocorrencias(self, uf, limite=0):
		if(limite != 0):
			limite = 'LIMIT %s' %limite
		else:
			limite = ''

		self.inicia_conexao()


		query = """SELECT tcodescricao, ocodataregistro, tmvdescricao, unidenominacao, ocodataocorrencia, uniendereco,
				ttudescricao, tmuuf, ocoid, tmudenominacao

				FROM ocorrencia, ocorrenciaveiculo, marcadeveiculo, tipoComunicacao, municipio, unidadeoperacional,
				tipounidadeoperacional, veiculo
	
				WHERE ocomunicipio = tmucodigo AND ocotipo = tcocodigo
				AND unimunicipio = tmucodigo AND unittucodigo = ttucodigo AND ocvocoid = ocoid
				AND veiid = ocvveiid AND tmvcodigo = veitmvcodigo AND tmuuf = \'%s\' %s;""" %(uf,limite)

		return self.executa_query(query)

if __name__ == '__main__':
	if(len(sys.argv)>1):
		ocorrencia = UfDAO(sys.argv[1])
	else:
		ocorrencia = UfDAO()
	print ocorrencia.listar_ocorrencias('DF', 5)


