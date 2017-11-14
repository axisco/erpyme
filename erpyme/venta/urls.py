from django.conf.urls import url

from . import views
app_name = 'venta'

urlpatterns = [
	#mantenedor proveedor
    url(r'^ver/$', views.index_ven, name='index_ven'),
    url(r'^nueva/$', views.nueva_ven, name='nueva_ven'),
    url(r'^detalle/(?P<id>[0-9]+)$', views.detalle_ven, name='detalle_ven'),
]
