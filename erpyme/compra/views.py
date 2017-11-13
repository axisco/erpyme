from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.forms.models import inlineformset_factory

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json

from django.db.models import Count
from mantenedor.models import Proveedor
from mantenedor.models import Producto
from mantenedor.models import Categoria
from .models import CompraProducto
from .models import ItemCompra

#form
from .forms import CompraProductoForm
from mantenedor.forms import ProveedorForm

#vistas proveedor
def index_com(request):
	lista = CompraProducto.objects.annotate(total_item=Count('itemcompra'))
	context = {
        	'lista': lista,
	        'titulo': "Compras",
    	}
	return render( request, 'compra/index.html', context)

def detalle_com(request, id):
    compra = CompraProducto.objects.get(pk=id)
    productos = ItemCompra.objects.filter(compraproducto=id)
    context = {
            'compra': compra,
            'productos' : productos,
            'titulo': "Detalle de Compra",
    }
    return render( request, 'compra/detalle.html', context)

def nueva_com(request):
    	lista = Proveedor.objects.order_by('rsocial')
    	context = {
            	'lista': lista,
    	        'titulo': "Compras",
        	}
    	return render( request, 'compra/index.html', context)
