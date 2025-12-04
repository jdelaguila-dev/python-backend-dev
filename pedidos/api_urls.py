from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CategoriaViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r"productos", ProductoViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"pedidos", PedidoViewSet)

urlpatterns = router.urls
