DROP TABLE IF EXISTS `ocorrencia`;
CREATE TABLE `ocorrencia`
( 
`ocoid` INT(11) unsigned NOT NULL, 
`ocolocal` INT(11) unsigned , 
`ocostatus` VARCHAR(255) , 
`ocomunicipio` INT(11) unsigned , 
`ocosentido` INT(11) unsigned , 
`ocodataocorrencia` VARCHAR(255) , 
`ocodataregistro` VARCHAR(255) , 
`ocotipo` VARCHAR(255) , 
`ococomid` INT(11) unsigned , 
`ocoidorigem` VARCHAR(255) , 
`ocodatafim` VARCHAR(255) ,
`sem` INT(11) unsigned ,
`ano` INT(11) unsigned 
-- PRIMARY KEY (`ocoid`, `sem`, `ano`)
) 
ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `pessoa`;
CREATE TABLE `pessoa`
 ( 
`pesid` INT(11) unsigned NOT NULL, 
`pesdatanascimento` VARCHAR(255) , 
`pesnaturalidade` VARCHAR(255) , 
`pesnacionalidade` VARCHAR(255) , 
`pessexo` VARCHAR(255) , 
`pesteccodigo` INT(11) unsigned , 
`pestgicodigo` INT(11) unsigned , 
`pesmunicipio` VARCHAR(255) , 
`pestopcodigo` VARCHAR(255) , 
`pesmunicipioori` VARCHAR(255) , 
`pespaisori` VARCHAR(255) , 
`pesmunicipiodest` VARCHAR(255) , 
`pespaisdest` VARCHAR(255) , 
`pesveiid` VARCHAR(255) , 
`pesestadofisico` INT(11) unsigned , 
`pescinto` VARCHAR(255) , 
`pescapacete` VARCHAR(255) , 
`peshabilitado` VARCHAR(255) , 
`pessocorrido` VARCHAR(255) , 
`pesdormindo` VARCHAR(255) , 
`pesalcool` VARCHAR(255) , 
`peskmpercorre` VARCHAR(255) , 
`peshorapercorre` VARCHAR(255) , 
`pescategcnh` VARCHAR(255) , 
`pesufcnh` VARCHAR(255) , 
`pespaiscnh` VARCHAR(255) , 
`pesdatahabil` VARCHAR(255) , 
`pesdatavalidade` VARCHAR(255) , 
`pesidade` VARCHAR(255) , 
`pesaltura` VARCHAR(255) , 
`pespeso` VARCHAR(255) , 
`pescicatriz` VARCHAR(255) , 
`pestatuagem` VARCHAR(255) , 
`pessinal` VARCHAR(255) , 
`peslesao` VARCHAR(255) , 
`pestcccodigo` VARCHAR(255) , 
`pestctcodigo` VARCHAR(255) , 
`pestclcodigo` VARCHAR(255) , 
`pesoenid` VARCHAR(255) ,
`sem` INT(11) unsigned ,
`ano` INT(11) unsigned 
 -- PRIMARY KEY (`pesid`, `sem`, `ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `ocorrenciaPessoa`;
CREATE TABLE `ocorrenciaPessoa`
 ( 
`opeid` INT(11) unsigned NOT NULL, 
`opeocoid` INT(11) unsigned , 
`opepesid` INT(11) unsigned , 
`opeportenumero` VARCHAR(255) , 
`opeportevalidade` VARCHAR(255) , 
`opettecodigo` INT(11) unsigned , 
`openaoident` VARCHAR(255) , 
`opeestrangeiro` VARCHAR(255) , 
`opeanexo` VARCHAR(255) , 
`opecondalegadas` VARCHAR(255) ,
`sem` INT(11) unsigned ,
`ano` INT(11) unsigned 
-- PRIMARY KEY (`opeid`, `sem`, `ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `ocorrenciaacidente`;
CREATE TABLE `ocorrenciaacidente`
 ( 
`oacocoid` INT(11) unsigned NOT NULL,
`oacttacodigo` INT(11) unsigned,
`oactcacodigo` INT(11) unsigned,
`oacdano` VARCHAR(255) ,
`oacdanoterc` VARCHAR(255) ,
`oacdanoamb` VARCHAR(255) ,
`oaclatitude` FLOAT ,
`oaclongitude` FLOAT ,
`oacdistab` FLOAT ,
`oacdistac` FLOAT ,
`oacdistbc` FLOAT ,
`oacmodelopista` INT(11) ,
`oacsentido1` VARCHAR(255) ,
`oacsentido2` VARCHAR(255) ,
`oacqtdfaixa1` INT(11) unsigned ,
`oacqtdfaixa2` INT(11) unsigned ,
`oacacostamento1` VARCHAR(255) ,
`oacacostamento2` VARCHAR(255) ,
`oaccanteiro` VARCHAR(255) ,
`oaclinhacentral` INT(11) unsigned ,
`oacorientpista` VARCHAR(255) ,
`oacgirafundo` VARCHAR(255) ,
`oacversaocroqui` INT(11) unsigned ,
`oacsitio` INT(11) unsigned,
`sem` INT(11) unsigned ,
`ano` INT(11) unsigned 
-- PRIMARY KEY (`oacocoid`, `sem`, `ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

DROP TABLE IF EXISTS `corveiculo`;
CREATE TABLE `corveiculo`
 ( 
`tcecodigo` INT(11) unsigned NOT NULL, 
`tcedescricao` VARCHAR(255) , 
`tceatualiza` VARCHAR(255) 
, PRIMARY KEY (`tcecodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; 

DROP TABLE IF EXISTS `localbr`;
CREATE TABLE IF NOT EXISTS `localbr`
 ( 
`lbrid` INT(11) unsigned , 
`lbruf` VARCHAR(255) , 
`lbrbr` INT(11) unsigned , 
`lbrkm` INT(11) unsigned , 
`lbrlatitude` VARCHAR(255) , 
`lbrlongitude` VARCHAR(255) , 
`lbrpnvid` INT(11) unsigned , 
`lbratualiza` VARCHAR(255) 
, PRIMARY KEY (`lbrid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; 

DROP TABLE IF EXISTS `marcadeveiculo`;
CREATE TABLE `marcadeveiculo`
 ( 
`tmvcodigo` INT(11) unsigned NOT NULL, 
`tmvdescricao` VARCHAR(255) , 
`tmvatualiza` VARCHAR(255) 
, PRIMARY KEY (`tmvcodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; 

DROP TABLE IF EXISTS `municipio`;
CREATE TABLE `municipio`
 ( 
`tmucodigo` INT(11) unsigned NOT NULL, 
`tmudenominacao` VARCHAR(255) , 
`tmuuf` VARCHAR(255) 
, PRIMARY KEY (`tmucodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; 

DROP TABLE IF EXISTS `estadofisico`;
CREATE TABLE IF NOT EXISTS `estadofisico`
 ( 
`esid` INT(11) unsigned NOT NULL, 
`estadofisico` VARCHAR(255)
, PRIMARY KEY (`esid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; 

DROP TABLE IF EXISTS `ocorrenciaveiculo`;
CREATE TABLE `ocorrenciaveiculo`
 ( 
`ocvid` INT(11) unsigned NOT NULL, 
`ocvocoid` INT(11) unsigned , 
`ocvveiid` INT(11) unsigned
, PRIMARY KEY (`ocvid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin; 