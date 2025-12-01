from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Producto, Categoria, Pedido
from ..serializers import ProductoSerializer, CategoriaSerializer, PedidoSerializer


# ViewSet: ¡Hace la magia completa!
# Crea automáticamente la lógica para: Listar, Crear, Ver Detalle, Actualizar y Borrar.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Filtrar por categoria
    filterset_fields = [
        "categoria"
    ]  # Permite filtrar productos por categoría (ejemplo: ?categoria=1)

    # Buscar por nombre o descripción
    search_fields = [
        "nombre",
        "descripcion",
    ]  # Permite buscar productos por nombre o descripción\

    # Ordenar por precio
    ordering_fields = [
        "precio"
    ]  # Permite ordenar productos por precio (ejemplo: ?ordering=precio o ?ordering=-precio)


# ViewSet para Categoría
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ViewSet para Pedido
# Aquí NO usamos ReadOnly. Si no tienes token, no ves nada.
# Son datos sensibles de clientes.
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    # AGREGAR ESTO (Ojo que es diferente al de productos):
    permission_classes = [IsAuthenticated]
