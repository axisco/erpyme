from django.db import models
import datetime

from django.db import models
from django.utils import timezone
from decimal import Decimal


class Proveedor(models.Model):
    rut = models.CharField(max_length=70)
    rsocial = models.CharField(max_length=70)
    giro = models.CharField(max_length=70)
    direccion = models.CharField(max_length=70)
    comuna = models.CharField(max_length=70)
    telefono = models.CharField(max_length=70)
    web = models.URLField(default="http://www.sitio.cl")
    email = models.EmailField(max_length=70)
    fecha = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.rsocial

class Cliente(models.Model):
    rut = models.CharField(max_length=70)
    rsocial = models.CharField(max_length=200)
    giro = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=70)
    contacto = models.CharField(max_length=70, null=True)
    email = models.EmailField(max_length=70, null=True)
    telefono = models.CharField(max_length=70, null=True)
    fecha = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.rsocial

class Categoria(models.Model):
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    cod_barra = models.CharField(max_length=70)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=300)
    stock = models.IntegerField(default=0)
    valor = models.IntegerField(default=0)
    descuento = models.DecimalField(max_digits=3,decimal_places=1, default=Decimal('00.0'))
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
                return self.nombre
