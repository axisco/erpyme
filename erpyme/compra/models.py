from django.db import models
import datetime
from django.utils import timezone
from decimal import Decimal
from mantenedor.models import Proveedor
from mantenedor.models import Producto

# Create your models here.
class CompraProducto(models.Model):
    factura = models.IntegerField(default=0)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    def __str__(self):
        return self.proveedor.rsocial

class ItemCompra(models.Model):
    unidades = models.IntegerField(default=0)
    valor_unidad = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    compraproducto = models.ForeignKey(CompraProducto, on_delete=models.CASCADE)
    def __str__(self):
        return self.producto.nombre
