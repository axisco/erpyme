from django.contrib import admin

from .models import Cliente
from .models import Proveedor
from .models import Contacto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Contacto)