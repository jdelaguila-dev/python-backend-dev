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

    # VALIDACIÓN POR CAMPO (validate_<nombre_campo>)
    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "El precio no puede ser gratuito. ¡Esto es un negocio!"
            )
        return value

    # VALIDACION DE OBJETO COMPLETO
    # Ejemplo: Si es de categoría 'Alcohol', debe tener una advertencia en la descripción
    def validate(self, data):
        # data es un diccionario con todos los campos enviados
        nombre = data.get("nombre", "")

        if (
            "alcohol" in nombre.lower()
            and "advertencia" not in data.get("descripcion", "").lower()
        ):
            raise serializers.ValidationError(
                "Los productos con alcohol deben incluir una advertencia en la descripción."
            )
        return data

    class Meta:
        model = Producto
        fields = "__all__"  # Trae id, nombre, precio, imagen, etc.

    # Para lectura, interceptamos y ponemos los datos bonitos
    def to_representation(self, instance):
        # Obtener la representación original
        response = super().to_representation(instance)
        # Modificar la representación del campo 'precio' para agregar el símbolo de moneda
        response["precio"] = f"${response['precio']}"
        # Devolver la representación modificada

        # reemplazar 'categoria' por campos específicos
        response["categoria"] = {
            "id": instance.categoria.id,
            "nombre": instance.categoria.nombre,
        }

        return response


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"  # Trae id, producto, nombre_cliente, direccion, fecha_registro, etc.
