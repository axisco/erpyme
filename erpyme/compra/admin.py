from django.contrib import admin

# Register your models here.
from .models import CompraProducto
from .models import ItemCompra

admin.site.register(CompraProducto)
admin.site.register(ItemCompra)
