from django.db import models
import datetime
from django.utils import timezone
from decimal import Decimal
from mantenedor.models import Cliente
from mantenedor.models import Producto

# Create your models here.
class VentaProducto(models.Model):
    tipo = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    def __str__(self):
        return "venta"

class ItemVenta(models.Model):
    unidades = models.IntegerField(default=0)
    valor_unidad = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ventaproducto = models.ForeignKey(VentaProducto, on_delete=models.CASCADE)
    def __str__(self):
        return self.producto.nombre
