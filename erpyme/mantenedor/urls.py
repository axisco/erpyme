from django.conf.urls import url

from . import views

app_name = 'proveedor'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<proveedor_id>[0-9]+)$', views.detalle, name='detalle'),
]