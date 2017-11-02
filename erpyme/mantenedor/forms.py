from django import forms

from .models import Cliente
from .models import Proveedor

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('rut','rsocial','giro','direccion','comuna','contacto','email','telefono')

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ('rut','rsocial','giro')
