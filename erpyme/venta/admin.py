from django.contrib import admin

# Register your models here.
from .models import VentaProducto
from .models import ItemVenta

admin.site.register(VentaProducto)
admin.site.register(ItemVenta)
