from django.db import models

# Create your models here.


# Crear modelo de Ingrediente
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    costo_extra = models.DecimalField(
        max_digits=4, decimal_places=2, default=0.0, blank=True, null=True
    )

    def __str__(self):
        return f"{self.nombre} - (${self.costo_extra})"


# 1. Crear el modelo Categoria
class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100, unique=True, verbose_name="Nombre de la Categoría"
    )
    descripcion = models.TextField(
        blank=True, null=True, verbose_name="Descripción de la Categoría"
    )

    # MÉTODOS MÁGICOS: __str__
    # Sin esto, Django nos mostrará "Categoria object (1)".
    # Con esto, nos mostrará "Bebidas".
    def __str__(self):
        return self.nombre


# 2. Crear el modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(
        blank=True, null=True, verbose_name="Descripción del Producto"
    )
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    # ForeignKey: Conecta Producto con Categoria.
    # on_delete=models.CASCADE: "Si elimino la categoría 'Bebidas', elimina todas las cocacolas".
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)
    # NUEVO CAMPO:
    # ManyToManyField crea una "Tabla Intermedia" invisible automáticamente.
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)

    # MÉTODOS MÁGICOS: __str__
    def __str__(self):
        return f"{self.nombre} - {self.categoria.nombre} (${self.precio:.2f})"


# 3. Crear el modelo Pedido
class Pedido(models.Model):
    # Relación: Si se borra el producto, se borra el pedido (CASCADE).
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    direccion = models.TextField()
    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )  # Fecha y hora de creación automática.

    def __str__(self):
        return f"Pedido de {self.nombre_cliente} - {self.producto.nombre}"
