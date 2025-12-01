from rest_framework import serializers
from .models import Ingrediente, Producto, Categoria, Pedido


# Muy parecido es a un ModelForm
class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ["id", "nombre", "costo_extra"]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"  # Trae id, nombre, descripcion, etc.


class ProductoSerializer(serializers.ModelSerializer):
    # Nested Serializer:
    # Al poner esto, en vez de devolver IDs [1, 2], devuelve Objetos [{nombre: "Queso"...}]
    # read_only=True: Para simplificar, hoy solo "leemos" ingredientes, no creamos ingredientes al crear productos.
    ingredientes = IngredienteSerializer(many=True, read_only=True)
    # Categoría también podría ser un nested serializer, pero hoy lo dejamos simple (ID).
    categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = "__all__"  # Trae id, nombre, precio, imagen, etc.


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"  # Trae id, producto, nombre_cliente, direccion, fecha_registro, etc.
