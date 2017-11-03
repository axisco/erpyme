from django.contrib import admin

# Register your models here.
from .models import Cliente
from .models import Proveedor
from .models import Producto
from .models import Categoria


admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Categoria)
