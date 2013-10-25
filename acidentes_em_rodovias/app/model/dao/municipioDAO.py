# -*- coding: utf-8 -*-

from new_dao import DAO

class MunicipioDAO:
	def __init__(self):
		pass

	def listar_ocorrencias(self, municipio, limite=0):
		if(limite != 0):
			limite = 'LIMIT %s' %limite
		else:
			limite = ''

		dao = DAO()
		dao.inicia_conexao()

		query = """SELECT tcodescricao, ocodataregistro, tmvdescricao, unidenominacao, ocodataocorrencia, uniendereco,
				ttudescricao, tmuuf, ocoid, tmudenominacao

				FROM ocorrencia, ocorrenciaveiculo, marcadeveiculo, tipoComunicacao, municipio, unidadeoperacional,
				tipounidadeoperacional, veiculo
	
				WHERE ocomunicipio = tmucodigo AND tmucodigo = %s AND ocotipo = tcocodigo
				AND unimunicipio = tmucodigo AND unittucodigo = ttucodigo AND ocvocoid = ocoid
				AND veiid = ocvveiid AND tmvcodigo = veitmvcodigo  %s;""" %(municipio,limite)

		return dao.executa_query(query)


if __name__ == '__main__':
	ocorrencia = MunicipioDAO()
	print ocorrencia.listar_ocorrencias(35, 5)