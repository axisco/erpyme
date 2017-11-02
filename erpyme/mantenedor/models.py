from django.db import models
import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=70)
    cargo = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    rut = models.CharField(max_length=70)
    rsocial = models.CharField(max_length=70)
    giro = models.CharField(max_length=70)
    direccion = models.CharField(max_length=70)
    comuna = models.CharField(max_length=70)
    telefono = models.CharField(max_length=70)
    nombre = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    contactos = models.ForeignKey(Contacto, on_delete=models.CASCADE)
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
