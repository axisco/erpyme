from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.forms.models import inlineformset_factory

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json

from django.db.models import Count
from mantenedor.models import Cliente
from mantenedor.models import Producto
from .models import VentaProducto
from .models import ItemVenta

def index_ven(request):
	lista = VentaProducto.objects.annotate(total_item=Count('itemventa'))
	context = {
        	'lista': lista,
	        'titulo': "Ventas",
    	}
	return render( request, 'venta/index.html', context)

def detalle_ven(request, id):
    venta = VentaProducto.objects.get(pk=id)
    productos = ItemVenta.objects.filter(ventaproducto=id)
    context = {
            'compra': venta,
            'productos' : productos,
            'titulo': "Detalle de Venta",
    }
    return render( request, 'venta/detalle.html', context)

def nueva_ven(request):
    	lista = Proveedor.objects.order_by('rsocial')
    	context = {
            	'lista': lista,
    	        'titulo': "Compras",
        	}
    	return render( request, 'venta/index.html', context)
