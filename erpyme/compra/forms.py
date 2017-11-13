from django import forms
from django.forms import ModelForm

from mantenedor.models import Cliente
from mantenedor.models import Proveedor
from mantenedor.models import Categoria
from mantenedor.models import Producto

from .models import CompraProducto
from .models import ItemCompra

class CompraProductoForm(forms.ModelForm):
    class Meta:
        model = CompraProducto
        fields = [
            "proveedor"
        ]
