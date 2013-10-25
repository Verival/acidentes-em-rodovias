# -*- coding: utf-8 -*-
import sys

from dao import DAO

class MunicipioDAO(DAO):
	def listar_ocorrencias(self, municipio, limite=0):
		if(limite != 0):
			limite = 'LIMIT %s' %limite
		else:
			limite = ''

		self.inicia_conexao()

		query = """SELECT tcodescricao, ocodataregistro, tmvdescricao, unidenominacao, ocodataocorrencia, uniendereco,
				ttudescricao, tmuuf, ocoid, tmudenominacao

				FROM ocorrencia, ocorrenciaveiculo, marcadeveiculo, tipoComunicacao, municipio, unidadeoperacional,
				tipounidadeoperacional, veiculo
	
				WHERE ocomunicipio = tmucodigo AND tmucodigo = %s AND ocotipo = tcocodigo
				AND unimunicipio = tmucodigo AND unittucodigo = ttucodigo AND ocvocoid = ocoid
				AND veiid = ocvveiid AND tmvcodigo = veitmvcodigo  %s;""" %(municipio,limite)

		return self.executa_query(query)


if __name__ == '__main__':
	if(len(sys.argv)>1):
		municipio = MunicipioDAO(sys.argv[1])
	else:
		municipio = MunicipioDAO()

	print municipio.listar_ocorrencias(35, 5)