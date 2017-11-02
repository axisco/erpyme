from django.conf.urls import url

from . import views
app_name = 'mantenedor'

urlpatterns = [
	#mantenedor proveedor
    url(r'^proveedor/$', views.index_pro, name='index_pro'),
	url(r'^proveedor/(?P<id>[0-9]+)$', views.detalle_pro, name='detalle_pro'),
    url(r'^proveedor/agregar$', views.agregar_pro, name='agregar_pro'),
    url(r'^proveedor/(?P<id>[0-9]+)/editar$', views.editar_pro, name='editar_pro'),

    #mantenedor cliente
	url(r'^cliente/$', views.index_cli, name='index_cli'),
    url(r'^cliente/(?P<id>[0-9]+)$', views.detalle_cli, name='detalle_cli'),
    url(r'^cliente/agregar$', views.agregar_cli, name='agregar_cli'),
    url(r'^cliente/(?P<id>[0-9]+)/editar$', views.editar_cli, name='editar_cli'),

]
