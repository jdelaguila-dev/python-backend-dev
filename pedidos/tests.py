import pytest
from .models import Producto, Categoria


# Decorador para acceder a la base de datos en las pruebas
@pytest.mark.django_db
def test_crear_producto():
    # 1. Setup: Crear datos previos necesarios
    categoria = Categoria.objects.create(nombre="Bebidas")

    # 2. Ejecución: Crear un nuevo producto
    producto = Producto.objects.create(
        nombre="Coca Cola",
        descripcion="Bebida gaseosa",
        precio=1.50,
        categoria=categoria,
    )

    # 3. Verificación: Comprobar que el producto se creó correctamente
    assert producto.id is not None
    assert producto.nombre == "Coca Cola"
    assert producto.categoria.nombre == "Bebidas"
    assert Producto.objects.count() == 1


@pytest.mark.django_db
def test_string_representation_producto():
    categoria = Categoria.objects.create(nombre="Hamburguesas")
    producto = Producto.objects.create(
        nombre="Burger",
        descripcion="Deliciosa hamburguesa con queso",
        precio=3.00,
        categoria=categoria,
    )

    # Verificamos que el __str__ funcione como dijimos ("Burger ($10.00)")
    assert str(producto) == "Burger - Hamburguesas ($3.00)"
