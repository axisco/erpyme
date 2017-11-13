from django.conf.urls import url

from . import views
app_name = 'compra'

urlpatterns = [
	#mantenedor proveedor
    url(r'^ver/$', views.index_com, name='index_com'),
    url(r'^nueva/$', views.nueva_com, name='nueva_com'),
    url(r'^detalle/(?P<id>[0-9]+)$', views.detalle_com, name='detalle_com'),
]
