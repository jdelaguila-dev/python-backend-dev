from django.contrib import admin

# Register your models here.

from .models import Categoria, Ingrediente, Producto, Pedido

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Ingrediente)


# Personalizar el Admin de Producto
class ProductoAdmin(admin.ModelAdmin):
    # filter_horizontal agrega un widget de JS para seleccionar ingredientes fácilmente
    filter_horizontal = ("ingredientes",)
    list_display = ("nombre", "precio", "categoria")  # Para ver columnas bonitas


# Re-registramos Producto con la configuración nueva
admin.site.unregister(Producto)  # Si ya estaba registrado simple, lo quitamos
admin.site.register(Producto, ProductoAdmin)
