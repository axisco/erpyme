from django.conf.urls import url

from . import views
app_name = 'venta'

urlpatterns = [
	#mantenedor proveedor
    url(r'^verBoleta/$', views.index_ver_bol, name='index_ver_bol'),
    # url(r'^ventaBoleta/$', views.nueva_bol, name='nueva_bol'),
    # url(r'^detalleBoleta/(?P<id>[0-9]+)$', views.detalle_bol, name='detalle_bol'),
    url(r'^verFactura/$', views.index_ver_fac, name='index_ver_fac'),
    # url(r'^ventaFactura/$', views.nueva_fac, name='nueva_fac'),
    # url(r'^detalleFactura/(?P<id>[0-9]+)$', views.detalle_fac, name='detalle_fac'),
]
