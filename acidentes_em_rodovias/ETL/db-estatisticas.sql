-- Cria e popula a tabela de estatísticas para tipos de ocorrência
DROP TABLE IF EXISTS `estatisticas_tipo`;
CREATE TABLE `estatisticas_tipo` (
  `idEstatisticaTipo` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) COLLATE latin1_general_ci NOT NULL,
  `quantidade_ocorrencias` int(11) NOT NULL,
  `ano` int(11) NOT NULL,
  PRIMARY KEY (`idEstatisticaTipo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

INSERT INTO  `estatisticas_tipo` (  `tipo` ,  `quantidade_ocorrencias` ,  `ano` ) 
SELECT ta.ttadescricao, COUNT(*) AS  'quantidade_ocorrencias', o.ano
FROM ocorrencia AS o
INNER JOIN ocorrenciaacidente AS oa ON o.ocoid = oa.oacocoid
INNER JOIN tipoAcidente AS ta ON oa.oacttacodigo = ta.ttacodigo
GROUP BY ta.ttadescricao, o.ano;

-- Cria e popula a tabela de estatísticas para causas de ocorrência
DROP TABLE IF EXISTS `estatisticas_causa`;
CREATE TABLE `estatisticas_causa` (
  `idEstatisticaCausa` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `causa` varchar(255) COLLATE latin1_general_ci NOT NULL,
  `quantidade_ocorrencias` int(11) NOT NULL,
  `ano` int(11) NOT NULL,
  PRIMARY KEY (`idEstatisticaCausa`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

INSERT INTO  `estatisticas_causa` (  `causa` ,  `quantidade_ocorrencias` ,  `ano` ) 
SELECT ca.tcadescricao, COUNT( * ) AS  'quantidade_ocorrencias', o.ano
FROM ocorrencia AS o
INNER JOIN ocorrenciaacidente AS oa ON o.ocoid = oa.oacocoid
INNER JOIN causaacidente AS ca ON oa.oactcacodigo = ca.tcacodigo
GROUP BY ca.tcadescricao, o.ano;