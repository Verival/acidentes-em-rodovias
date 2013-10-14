from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'acidentes_em_rodovias.controller.home', name='home'),
    # url(r'^acidentes_em_rodovias/', include('acidentes_em_rodovias.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^acidentes_rodovias/$', 'app.controller.index'),
    url(r'^acidentes_rodovias/regiao$', 'app.controller.consulta_por_regiao'),
    url(r'^acidentes_rodovias/periodo$', 'app.controller.consulta_por_periodo'),
    url(r'^acidentes_rodovias/pessoa$', 'app.controller.consulta_por_pessoa'),
    url(r'^acidentes_rodovias/rodovia$', 'app.controller.consulta_por_rodovia'),
    url(r'^acidentes_rodovias/consulta/(?P<tipo_consulta>\w+)$', 'app.controller.executa_consulta'),
)