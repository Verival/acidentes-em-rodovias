from windmill.authoring import WindmillTestClient

def test_tests_acidentes_rodovias_numero_ocorrencias_envolvidos_windmill():
    client = WindmillTestClient(__name__)

    client.asserts.assertNode(link=u'Estat\xedsticas')
    client.asserts.assertNode(link=u'N\xfamero de ocorr\xeancias/envolvidos')
    client.click(link=u'N\xfamero de ocorr\xeancias/envolvidos')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertText(xpath=u'/html/body/div[2]/div/div/h4/center', validator=u'Estat\xedsticas - Ocorr\xeancias e envolvidos')
    client.asserts.assertNode(link=u'Quantidade de acidentes e envolvidos ao longo dos anos')
    client.asserts.assertText(xpath=u'/html/body/div[3]/div/section[1]/p', validator=u'Quantidade de acidentes e envolvidos ao longo dos anos')
    client.asserts.assertNode(id=u'grafico_coluna')
    client.asserts.assertNode(link=u'M\xe9dia de envolvidos por acidente e desvio padr\xe3o')
    client.asserts.assertText(xpath=u'/html/body/div[3]/div/section[2]/p', validator=u'M\xe9dia de envolvidos por acidente e desvio padr\xe3o')
    client.asserts.assertNode(id=u'grafico_linha_area')