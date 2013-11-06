# -*- coding: utf-8 -*-

from generico_dao import GenericoDAO
from models.ocorrencia_basica import *

class OcorrenciaBasicaDAO(GenericoDAO):
	def lista_ocorrencias_por_regiao(self, municipio_id, limite=0):
		if(limite != 0):
			limite = 'LIMIT %s' % limite
		else:
			limite = ''
		try:
			query = """SELECT oco.ocoid, oco.ocodataocorrencia, oco.ocodataregistro, 
				tmu.tmudenominacao, tmu.tmuuf, tco.tcodescricao, tta.ttadescricao,
				tca.tcadescricao, lbr.lbrbr, tmv.tmvdescricao, tvv.tvvdescricao
				FROM ocorrencia oco
				INNER JOIN municipio tmu ON  tmu.tmucodigo =  oco.ocomunicipio 
				INNER JOIN tipoComunicacao tco ON tco.tcocodigo = oco.ocotipo
				INNER JOIN localbr lbr ON lbr.lbrid = oco.ocolocal
				INNER JOIN ocorrenciaacidente oac ON oac.oacocoid = oco.ocoid
				INNER JOIN tipoAcidente tta ON tta.ttacodigo = oac.oacttacodigo
				INNER JOIN causaacidente tca ON tca.tcacodigo = oac.oactcacodigo
				INNER JOIN ocorrenciaveiculo ocv ON ocv.ocvid = oco.ocoid
				INNER JOIN veiculo vei ON ocv.ocvveiid = vei.veiid
				INNER JOIN marcadeveiculo tmv ON vei.veitmvcodigo = tmv.tmvcodigo
				INNER JOIN tipoveiculo tvv ON vei.veitvvcodigo = tvv.tvvcodigo
				WHERE oco.ocomunicipio = %s 
				%s;""" %(municipio_id, limite)
		except OperationError as e:
			sys.stderr.write("Falha na comunicação: " + str(e))
			return None
		except InternalError as e:
			sys.stderr.write("Erro de sincronia: " + str(e))
			return None
		except NotSuportedError as e:
			sys.stderr.write("Operação não suportada: " + str(e))
			return None
		return self.transforma_dicionario_em_objetos(self.executa_query(query), "OcorrenciaBasica", "ocorrencia_basica")

	def lista_ocorrencias_por_periodo(self, data_inicio, data_fim, limite=0):
		if(limite != 0):
			limite = 'LIMIT %s' % limite
		else:
			limite = ''

		data_inicio = data_inicio + ' 00:00:00'
		data_fim = data_fim + ' 23:59:59'

		
		query = """SELECT oco.ocoid, oco.ocodataocorrencia, oco.ocodataregistro, 
				tmu.tmudenominacao, tmu.tmuuf, tco.tcodescricao, tta.ttadescricao,
				tca.tcadescricao, lbr.lbrbr, tmv.tmvdescricao, tvv.tvvdescricao
				FROM ocorrencia oco
				INNER JOIN municipio tmu ON  tmu.tmucodigo =  oco.ocomunicipio 
				INNER JOIN tipoComunicacao tco ON tco.tcocodigo = oco.ocotipo
				INNER JOIN localbr lbr ON lbr.lbrid = oco.ocolocal
				INNER JOIN ocorrenciaacidente oac ON oac.oacocoid = oco.ocoid
				INNER JOIN tipoAcidente tta ON tta.ttacodigo = oac.oacttacodigo
				INNER JOIN causaacidente tca ON tca.tcacodigo = oac.oactcacodigo
				INNER JOIN ocorrenciaveiculo ocv ON ocv.ocvid = oco.ocoid
				INNER JOIN veiculo vei ON ocv.ocvveiid = vei.veiid
				INNER JOIN marcadeveiculo tmv ON vei.veitmvcodigo = tmv.tmvcodigo
				INNER JOIN tipoveiculo tvv ON vei.veitvvcodigo = tvv.tvvcodigo
				WHERE oco.ocodataocorrencia >= STR_TO_DATE('{0}', '%d/%m/%Y %H:%i:%s') 
				AND oco.ocodataocorrencia <= STR_TO_DATE('{1}', '%d/%m/%Y %H:%i:%s')
				{2}
				;""".format(data_inicio, data_fim, limite)
		
		return self.transforma_dicionario_em_objetos(self.executa_query(query), "OcorrenciaBasica", "ocorrencia_basica")
