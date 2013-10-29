SET FOREIGN_KEY_CHECKS=0;

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
`ano` INT(11) unsigned ,
PRIMARY KEY (`ocoid`, `sem`, `ano`)
) 
ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

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
`ano` INT(11) unsigned ,
PRIMARY KEY (`oacocoid`, `sem`, `ano`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

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
`ano` INT(11) unsigned ,
 PRIMARY KEY (`opeid`, `sem`, `ano`) 
 -- CONSTRAINT FOREIGN KEY (`opeocoid`, `sem`, `ano`) REFERENCES `ocorrencia` (`ocoid`, `sem`, `ano`),
 -- CONSTRAINT FOREIGN KEY (`opepesid`, `sem`, `ano`) REFERENCES `pessoa` (`pesid`, `sem`, `ano`),
 -- CONSTRAINT FOREIGN KEY (`opettecodigo`) REFERENCES `tipoenvolvido` (`ttecodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

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
 PRIMARY KEY (`pesid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `causaacidente`;
CREATE TABLE `causaacidente`
(
`tcacodigo` INT(11) NOT NULL, 
`tcadescricao` VARCHAR(255),
PRIMARY KEY(`tcacodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `unidadeoperacional`;
CREATE TABLE `unidadeoperacional`
(
`uniid` INT(11) unsigned NOT NULL, 
`uniunidade` VARCHAR(255),
`unilotacao` VARCHAR(255),
`unisigla` VARCHAR(255),
`unittucodigo` INT(11),
`uniunidaderesponsavel` INT(11),
`unidenominacao` VARCHAR(255),
`uniendereco` VARCHAR(255),
`unimunicipio` VARCHAR(255),
`unicep` VARCHAR(255),
`unitelefone` VARCHAR(255),
`uniemail` VARCHAR(255),
`unilocal` INT(11),
`unilatitude` FLOAT,
`unilongitude` FLOAT,
`unihelicoptero` VARCHAR(255),
`unitexto` VARCHAR(255),
PRIMARY KEY(`uniid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `uf`;
CREATE TABLE `uf`
(
`tufuf` VARCHAR(2) NOT NULL, 
`tufdenominacao` VARCHAR(255),
PRIMARY KEY(`tufuf`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `veiculo`;
CREATE TABLE `veiculo`
(
`veiid` INT(11) unsigned NOT NULL, 
`vei.veiano` INT(11),
`veitmvcodigo` INT(11),
`veiqtdocupantes` INT(11),
`veitevcodigo` INT(11),
`veitcvcodigo` INT(11),
`veitvvcodigo` INT(11),
`veidescricao` VARCHAR(255),
`veimunicipio` INT(11),
`veitcecodigo` INT(11),
`veimunorigem` INT(11),
`veipaisorigem` INT(11),
`veimundestino` INT(11),
`veipaisdestino` INT(11),
`veitttcodigo` INT(11),
`veitipoproprietario` INT(11),
`veiproprietario` INT(11),
`veioenid` INT(11),
`veisequencial` INT(11),
`veitipoplaca` VARCHAR(255),
PRIMARY KEY(`veiid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `corveiculo`;
CREATE TABLE `corveiculo`
 ( 
`tcecodigo` INT(11) unsigned NOT NULL, 
`tcedescricao` VARCHAR(255) , 
`tceatualiza` VARCHAR(255) 
, PRIMARY KEY (`tcecodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci; 

DROP TABLE IF EXISTS `localbr`;
CREATE TABLE `localbr`
 ( 
`lbrid` INT(11) unsigned NOT NULL, 
`lbruf` VARCHAR(255) , 
`lbrbr` INT(11) unsigned , 
`lbrkm` INT(11) unsigned , 
`lbrlatitude` VARCHAR(255) , 
`lbrlongitude` VARCHAR(255) , 
`lbrpnvid` INT(11) unsigned , 
`lbratualiza` VARCHAR(255) 
, PRIMARY KEY (`lbrid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci; 

DROP TABLE IF EXISTS `marcadeveiculo`;
CREATE TABLE `marcadeveiculo`
 ( 
`tmvcodigo` INT(11) unsigned NOT NULL, 
`tmvdescricao` VARCHAR(255) , 
`tmvatualiza` VARCHAR(255) 
, PRIMARY KEY (`tmvcodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci; 

DROP TABLE IF EXISTS `municipio`;
CREATE TABLE `municipio`
 ( 
`tmucodigo` INT(11) unsigned NOT NULL, 
`tmudenominacao` VARCHAR(255) , 
`tmuuf` VARCHAR(255) 
, PRIMARY KEY (`tmucodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci; 

DROP TABLE IF EXISTS `estadofisico`;
CREATE TABLE IF NOT EXISTS `estadofisico`
 ( 
`esid` INT(11) unsigned NOT NULL, 
`estadofisico` VARCHAR(255)
, PRIMARY KEY (`esid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci; 

DROP TABLE IF EXISTS `ocorrenciaveiculo`;
CREATE TABLE `ocorrenciaveiculo`
 ( 
`ocvid` INT(11) unsigned NOT NULL, 
`ocvocoid` INT(11) unsigned , 
`ocvveiid` INT(11) unsigned
, PRIMARY KEY (`ocvid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci; 


DROP TABLE IF EXISTS `tipoAcidente`;
CREATE TABLE `tipoAcidente`
(
`ttacodigo` INT(11) unsigned NOT NULL, 
`ttadescricao` VARCHAR(255) ,
`ttaatualiza` VARCHAR(255) ,
`ttarelacidente` VARCHAR(255) ,
`ttaativo` VARCHAR(255) ,
PRIMARY KEY(`ttacodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipoApreensao`;
CREATE TABLE `tipoApreensao`
(
`ttpcodigo` VARCHAR(255) ,
`ttpdescricao` VARCHAR(255) ,
`ttpatualiza` VARCHAR(255) ,
PRIMARY KEY(`ttpcodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipoAreaEspecial`;
CREATE TABLE `tipoAreaEspecial`
(
`taecodigo` VARCHAR(255) ,
`taedescricao` VARCHAR(255) ,
`taeatualiza` VARCHAR(255) ,
PRIMARY KEY(`taecodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipoComunicacao`;
CREATE TABLE `tipoComunicacao`
(
`tcocodigo` VARCHAR(255) ,
`tcodescricao` VARCHAR(255) ,
`tcoatualiza` VARCHAR(255) ,
PRIMARY KEY(`tcocodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipocrime`;
CREATE TABLE `tipocrime`
(
`ttccodigo` VARCHAR(255) ,
`ttcdescricao` VARCHAR(255) ,
`ttcatualiza` VARCHAR(255) ,
PRIMARY KEY(`ttccodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipodetencao`;
CREATE TABLE `tipodetencao`
(
`ttdcodigo` VARCHAR(255) ,
`ttddescricao` VARCHAR(255) ,
`ttdatualiza` VARCHAR(255) ,
`ttdrelacidente` VARCHAR(255) ,
PRIMARY KEY(`ttdcodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipodocumento`;
CREATE TABLE `tipodocumento`
(
`ttocodigo` INT(11) unsigned NOT NULL, 
`ttodescricao` VARCHAR(255) ,
`ttoatualiza` VARCHAR(255) ,
`ttorelapreensao` VARCHAR(255) ,
`ttorelrecuperacao` VARCHAR(255) ,
PRIMARY KEY(`ttocodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipoenvolvido`;
CREATE TABLE `tipoenvolvido`
(
`ttecodigo` INT(11) unsigned NOT NULL, 
`ttedescricao` VARCHAR(255) ,
`tteatualiza` VARCHAR(255) ,
`tteativo` VARCHAR(255) ,
PRIMARY KEY(`ttecodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipolocalidade`;
CREATE TABLE `tipolocalidade`
(
`ttlcodigo` INT(11) unsigned NOT NULL, 
`ttldescricao` VARCHAR(255) ,
`ttlatualiza` VARCHAR(255) ,
PRIMARY KEY(`ttlcodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipoobra`;
CREATE TABLE `tipoobra`
(
`ttbcodigo` INT(11) unsigned NOT NULL, 
`ttbdescricao` VARCHAR(255) ,
`ttbatualiza` VARCHAR(255) ,
PRIMARY KEY(`ttbcodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipopontomedico`;
CREATE TABLE `tipopontomedico`
(
`ttmcodigo` INT(11) unsigned NOT NULL, 
`ttmdescricao` VARCHAR(255) ,
`ttmatualiza` VARCHAR(255) ,
PRIMARY KEY(`ttmcodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipopontonotavel`;
CREATE TABLE `tipopontonotavel`
(
`ttncodigo` INT(11) unsigned NOT NULL, 
`ttndescricao` VARCHAR(255) ,
`ttnatualiza` VARCHAR(255) ,
PRIMARY KEY(`ttncodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tiporeceptor`;
CREATE TABLE `tiporeceptor`
(
`ttrcodigo` INT(11) unsigned NOT NULL, 
`ttrdescricao` VARCHAR(255) ,
`ttratualiza` VARCHAR(255) ,
`ttrdelegacia` VARCHAR(255) ,
PRIMARY KEY(`ttrcodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tiposinalizacao`;
CREATE TABLE `tiposinalizacao`
(
`ttscodigo` INT(11) unsigned NOT NULL, 
`ttsdescricao` VARCHAR(255) ,
`ttsatualiza` VARCHAR(255) ,
PRIMARY KEY(`ttscodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipounidadeoperacional`;
CREATE TABLE `tipounidadeoperacional`
(
`ttucodigo` VARCHAR(255) ,
`ttudescricao` VARCHAR(255) ,
`ttuatualiza` VARCHAR(255) ,
PRIMARY KEY(`ttucodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `tipoveiculo`;
CREATE TABLE `tipoveiculo`
(
`tvvcodigo` INT(11) unsigned NOT NULL, 
`tvvdescricao` VARCHAR(255) ,
`tvvatualiza` VARCHAR(255) ,
`tvvrelacidente` VARCHAR(255) ,
`tvvativo` VARCHAR(255) ,
PRIMARY KEY(`tvvcodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `pnv`;
CREATE TABLE `pnv`
(
`pnv_id` INT(11) unsigned NOT NULL, 
`codigo` VARCHAR(255) ,
`descricao_dnit` VARCHAR(255) ,
`descricao_dprf` VARCHAR(255) ,
`br` INT(11) unsigned ,
`uf` VARCHAR(2) ,
`km_inicial` INT(11) unsigned , 
`km_fim` INT(11) unsigned , 
`extensao` INT(11) unsigned , 
`superficie_br` VARCHAR(255) ,
PRIMARY KEY(`pnv_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

DROP TABLE IF EXISTS `paises`;
CREATE TABLE `paises`
(
`tpacodigo` INT(11) unsigned NOT NULL,
`tpadescricao` VARCHAR(255) ,
PRIMARY KEY(`tpacodigo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci;

SET FOREIGN_KEY_CHECKS=1;