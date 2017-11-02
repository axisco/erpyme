from django.shortcuts import render
from django.http import Http404

from .models import Proveedor, Cliente

# Create your views here.

def index(request):
    lista_proveedores = Proveedor.objects.order_by('nombre')
    context = {
        'lista_proveedores': lista_proveedores,
        'titulo': "Proveedores",
    }
    return render( request, 'proveedor/index.html', context)

def detalle(request, proveedor_id):
    try:
        proveedor = Proveedor.objects.get(pk=proveedor_id)
        context = {
            'proveedor' : proveedor,
            'titulo': "Proveedor",
        }
        
    except Proveedor.DoesNotExist:
        raise Http404("Proveedor no existe")
    return render(request, 'proveedor/detalle.html', context)