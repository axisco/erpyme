from django import forms
from django.forms import ModelForm

from .models import Cliente
from .models import Proveedor
from .models import Categoria
from .models import Producto


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('rut','rsocial','giro','direccion','comuna','contacto','email','telefono')


class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ('rut','rsocial','giro','direccion','comuna','telefono','web','email')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            "nombre",
            "descripcion"
        ]

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "cod_barra",
            "nombre",
            "descripcion",
            "stock",
            "valor",
            "descuento",
            "categoria",
            "proveedor"
        ]
