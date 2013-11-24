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

-- Cria e popula a tabela de estatísticas para quantidade de envolvidos
DROP TABLE IF EXISTS `estatisticas_envolvido`;
CREATE TABLE `estatisticas_envolvido` (
  `idEstatisticaEnvolvido` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `quantidade_envolvidos` int(11),
  `quantidade_acidentes` int(11),
  `ano` int(11) UNIQUE,
  PRIMARY KEY (`idEstatisticaEnvolvido`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

INSERT INTO  `estatisticas_envolvido` (  `quantidade_envolvidos` ,  `ano` ) 
SELECT COUNT(*) AS 'quantidade_envolvidos', o.ano AS ano
FROM ocorrencia AS o
INNER JOIN ocorrenciaPessoa AS op ON op.opeocoid = o.ocoid
GROUP BY o.ano;
INSERT INTO  `estatisticas_envolvido` (  `quantidade_acidentes` ,  `ano` )
SELECT COUNT(*) as 'quantidade_acidentes', o.ano
FROM ocorrencia AS o
GROUP BY o.ano
ON DUPLICATE KEY UPDATE `quantidade_acidentes` = VALUES(  `quantidade_acidentes`  );

-- Cria e popula a tabela de estatísticas para uf por ocorrência
DROP TABLE IF EXISTS `estatisticas_uf`;
CREATE TABLE `estatisticas_uf` (
  `idEstatisticaUf` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uf` CHAR(2) COLLATE latin1_general_ci NOT NULL,
  `quantidade_ocorrencias` int(11) NOT NULL,
  `ano` int(11) NOT NULL,
  PRIMARY KEY (`idEstatisticaUf`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;
INSERT INTO estatisticas_uf
    (`quantidade_ocorrencias`, `uf`,`ano`)
SELECT
    COUNT(*) AS quantidade_ocorrencias,
    uf.tufuf,
    oco.ano
FROM ocorrencia oco
INNER JOIN localbr lbr
    ON lbr.lbrid = oco.ocoid
INNER JOIN uf
    ON uf.tufuf = lbr.lbruf
GROUP BY uf.tufuf, oco.ano
ORDER BY uf.tufuf, oco.ano

-- Cria e popula a tabela de estatísticas para br por ocorrência
DROP TABLE IF EXISTS `estatisticas_br`;
CREATE TABLE `estatisticas_br` (
  `idEstatisticaBr` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `br` CHAR(2) COLLATE latin1_general_ci NOT NULL,
  `quantidade_ocorrencias` int(11) NOT NULL,
  `ano` int(11) NOT NULL,
  PRIMARY KEY (`idEstatisticaUf`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;
INSERT INTO estatisticas_uf
    (`quantidade_ocorrencias`, `uf`,`ano`)
SELECT
    COUNT(*) AS quantidade_ocorrencias,
    lbr.lbrbr,
    oco.ano
FROM ocorrencia oco
INNER JOIN localbr lbr
    ON lbr.lbrid = oco.ocoid
GROUP BY lbr.lbrbr, oco.ano
ORDER BY lbr.lbrbr, oco.ano

-- Cria e popula a tabela de estatísticas para br por ocorrência
DROP TABLE IF EXISTS `estatisticas_br`;
CREATE TABLE `estatisticas_br` (
  `idEstatisticaBr` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `br` VARCHAR(3) COLLATE latin1_general_ci NOT NULL,
  `quantidade_ocorrencias` int(11) NOT NULL,
  `ano` int(11) NOT NULL,
  PRIMARY KEY (`idEstatisticaBr`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;
INSERT INTO estatisticas_br
    (`quantidade_ocorrencias`, `br`,`ano`)
SELECT
    COUNT(*) AS quantidade_ocorrencias,
    LPAD(lbr.lbrbr, 3, '0') AS br,
    oco.ano
FROM ocorrencia oco
INNER JOIN localbr lbr
    ON lbr.lbrid = oco.ocoid
WHERE lbr.lbrbr IS NOT NULL
GROUP BY lbr.lbrbr, oco.ano
ORDER BY lbr.lbrbr, oco.ano