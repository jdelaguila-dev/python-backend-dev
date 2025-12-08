from rest_framework import viewsets, filters as drf_filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters import rest_framework as filters

from pedidos.pagination import PaginacionGrande

from ..models import Producto, Categoria, Pedido
from ..serializers import ProductoSerializer, CategoriaSerializer, PedidoSerializer


# Definimos una clase para filtros avanzados
class ProductoFilter(filters.FilterSet):
    # Filtro de rango de precio (min y max)
    precio_min = filters.NumberFilter(
        field_name="precio", lookup_expr="gte"
    )  # precio >= X
    precio_max = filters.NumberFilter(
        field_name="precio", lookup_expr="lte"
    )  # precio <= X

    # Filtro por ingrediente (ManyToMany)
    # Permite buscar productos que tengan cierto ingrediente (Ej: ?ingrediente=Tocino)
    ingrediente = filters.CharFilter(
        field_name="ingredientes__nombre", lookup_expr="icontains"
    )

    class Meta:
        model = Producto
        fields = ["categoria", "precio_min", "precio_max", "ingrediente"]


# ViewSet: ¡Hace la magia completa!
# Crea automáticamente la lógica para: Listar, Crear, Ver Detalle, Actualizar y Borrar.
class ProductoViewSet(viewsets.ModelViewSet):
    # ANTES (Malo):
    # queryset = Producto.objects.all()

    # AHORA (Optimizado):
    # select_related -> Para ForeignKeys (1:N) -> Ej: Categoria
    # prefetch_related -> Para ManyToMany (N:N) -> Ej: Ingredientes
    queryset = (
        Producto.objects.all()
        .select_related("categoria")
        .prefetch_related("ingredientes")
    )
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 1. Activamos los backends de filtrado
    filter_backends = [
        filters.DjangoFilterBackend,  # Para nuestros filtros de campos (precio, categoria)
        drf_filters.SearchFilter,  # Para ?search= (Texto)
        drf_filters.OrderingFilter,  # Para ?ordering= (Orden)
    ]

    # Usamos nuestra clase de filtros personalizada
    filterset_class = ProductoFilter

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
    # ESTO ANULA LA PAGINACIÓN GLOBAL
    # Al poner None, DRF ignora el settings.py y devuelve la lista plana [{}, {}, {}]
    pagination_class = None


# ViewSet para Pedido
# Aquí NO usamos ReadOnly. Si no tienes token, no ves nada.
# Son datos sensibles de clientes.
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    # queryset = Pedido.objects.all().select_related("producto")

    serializer_class = PedidoSerializer
    # AGREGAR ESTO (Ojo que es diferente al de productos):
    permission_classes = [IsAuthenticated]
    # ✅ USAR TU PAGINACIÓN ESPECÍFICA
    pagination_class = PaginacionGrande
