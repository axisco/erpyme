from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.forms.models import inlineformset_factory

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json

#modelos
from .models import Proveedor
from .models import Cliente
from .models import Producto
from .models import Categoria


#form
from .forms import ClienteForm
from .forms import ProveedorForm
from .forms import ProductoForm
from .forms import CategoriaForm



#vistas proveedor
def index_pro(request):
	lista = Proveedor.objects.order_by('rsocial')
	context = {
        	'lista': lista,
	        'titulo': "Proveedores",
    	}
	return render( request, 'mantenedor/proveedor/index.html', context)

def detalle_pro(request, id):
	try:
			proveedor = Proveedor.objects.get(pk=id)
			context = {
			'proveedor' : proveedor,
			'titulo': "Proveedor",
    	}
	except Proveedor.DoesNotExist:
		raise Http404("Proveedor no existe")
	return render(request, 'mantenedor/proveedor/detalle.html', context)

def agregar_pro(request):
	if request.method == "POST":
		form = ProveedorForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/mantenedor/proveedor')
	else:
		form = ProveedorForm()
	return render( request,'mantenedor/proveedor/agregar.html', {'form': form})

def agregar_pro_pp(request):
	form = ProveedorForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_proveedor");</script>' % (instance.id, instance))
	return render(request, "mantenedor/proveedor/agregar.html", {"form" : form})

def editar_pro(request, id):
	proveedor = get_object_or_404(Proveedor,pk=id)
	if request.method == "POST":
		form = ProveedorForm(request.POST, instance=proveedor)
		if form.is_valid():
			form.save()
			return redirect('/mantenedor/proveedor')
	else:
		form = ProveedorForm(instance=proveedor)
	return render( request,'mantenedor/proveedor/agregar.html', {'form': form})

#vistas cliente
def index_cli(request):
	lista = Cliente.objects.order_by('rut')
	context = {
		'lista': lista,
		'titulo': "Clientes",
        }
	return render( request, 'mantenedor/cliente/index.html', context)

def detalle_cli(request, id):
		cliente = get_object_or_404(Cliente,pk=id)
		context = {
			'cliente' : cliente,
			'titulo': "Cliente",
		}
		return render(request, 'mantenedor/cliente/detalle.html', context)

def agregar_cli(request):
	if request.method == "POST":
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/mantenedor/cliente')
	else:
		form = ClienteForm()
	return render( request,'mantenedor/cliente/agregar.html', {'form': form})

def editar_cli(request, id):
	cliente = get_object_or_404(Cliente,pk=id)
	if request.method == "POST":
		form = ClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
			return redirect('/mantenedor/cliente')
	else:
		form = ClienteForm(instance=cliente)
	return render( request,'mantenedor/cliente/agregar.html', {'form': form})

#vistas producto
def index_prd(request):
	lista = Producto.objects.order_by('nombre')
	context = {
		'lista': lista,
		'titulo': "Productos",
        }
	return render( request, 'mantenedor/producto/index.html', context)

def detalle_prd(request, id):
		producto = get_object_or_404(Producto,pk=id)
		context = {
			'producto' : producto,
			'titulo': "Producto",
		}
		return render(request, 'mantenedor/producto/detalle.html', context)

def agregar_prd(request):
	form = ProductoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/mantenedor/producto')
	return render( request,'mantenedor/producto/agregar.html', {'form': form})

def agregar_cat_prd(request):
	form = CategoriaForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_categoria");</script>' % (instance.id, instance))
	return render(request, "mantenedor/producto/categoria.html", {"form" : form})

def editar_prd(request, id):
	producto = get_object_or_404(Producto,pk=id)
	if request.method == "POST":
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
			return redirect('/mantenedor/producto')
	else:
		form = ProductoForm(instance=producto)
	return render( request,'mantenedor/producto/agregar.html', {'form': form})
