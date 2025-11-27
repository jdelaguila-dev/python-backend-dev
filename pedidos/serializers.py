from rest_framework import serializers
from .models import Producto, Categoria, Pedido


# Muy parecido es a un ModelForm
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"  # Trae id, nombre, precio, imagen, etc.


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"  # Trae id, nombre, descripcion, etc.


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"  # Trae id, producto, nombre_cliente, direccion, fecha_registro, etc.
