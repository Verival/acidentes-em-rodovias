from windmill.authoring import WindmillTestClient

def test_tests_acidentes_rodovias_tipo_de_acidente_windmill():
    client = WindmillTestClient(__name__)

    client.asserts.assertNode(link=u'Estat\xedsticas')
    client.asserts.assertNode(link=u'Tipos de acidentes')
    client.click(link=u'Tipos de acidentes')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertText(xpath=u'/html/body/div[2]/div/div/h4/center', validator=u'Estat\xedsticas - Tipo de acidente')
    client.asserts.assertNode(link=u'Tipos de acidente ao longo dos anos')
    client.asserts.assertText(xpath=u'/html/body/div[3]/div/section[1]/p', validator=u'Tipos de acidente ao longo dos anos')
    client.asserts.assertNode(id=u'grafico_linha')
    client.asserts.assertNode(link=u'Porcentagem de acidentes j\xe1 registrados de acordo com o tipo')
    client.asserts.assertText(xpath=u'/html/body/div[3]/div/section[2]/p', validator=u'Porcentagem de acidentes j\xe1 registrados de acordo com o tipo')
    client.asserts.assertNode(id=u'grafico_torta')
    client.asserts.assertNode(link=u'M\xe9dia e desvio padr\xe3o de cada tipo de acidente')
    client.asserts.assertText(xpath=u'/html/body/div[3]/div/section[3]/p', validator=u'M\xe9dia e desvio padr\xe3o de cada tipo de acidente')
    client.asserts.assertNode(id=u'grafico_coluna')
    client.asserts.assertNode(link=u'Probabilidade para cada tipo de acidente no pr\xf3ximo ano')
    client.asserts.assertText(xpath=u'/html/body/div[3]/div/section[4]/p', validator=u'Probabilidade para cada tipo de acidente no pr\xf3ximo ano')
    client.asserts.assertNode(id=u'grafico_barra')