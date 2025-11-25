from django.contrib import admin

# Register your models here.

from .models import Categoria, Producto, Pedido

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Pedido)