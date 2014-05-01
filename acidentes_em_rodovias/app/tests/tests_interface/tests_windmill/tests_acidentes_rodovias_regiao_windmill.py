from windmill.authoring import WindmillTestClient

def test_acidentes_rodovias_regiao():
    client = WindmillTestClient(__name__)

    client.asserts.assertNode(link=u'Regi\xe3o')
    client.click(link=u'Regi\xe3o')
    client.waits.forPageLoad(timeout=u'20000')
    client.select(option=u'S\xe3o Paulo', id=u'customDropdown')
    client.asserts.assertNode(xpath=u'/html/body/form/div/div[1]/div/ul/li[26]')
    client.click(id=u'btn_submit')
    client.waits.forPageLoad(timeout=u'20000')
    client.asserts.assertNode(xpath=u'/html/body/form/div/div[1]/div/ul/li[60]')
    client.select(option=u'SAO JOSE DO RIO PRETO', id=u'customDropdown')
    client.click(id=u'btn_submit')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forPageLoad(timeout=u'5000')
    client.asserts.assertNode(link=u'SAO JOSE DO RIO PRETO')
    client.asserts.assertNode(link=u'SP')
    client.asserts.assertNode(xpath=u'/html/body/div[3]/div[1]/div/div/div[1000]/p[5]')