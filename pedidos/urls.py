from django.urls import path
from .views import menu_view, realizar_pedido_view, detalle_producto_view

urlpatterns = [
    # Ruta vacía '' significa: www.burgerqueen.com/pedidos/
    path('', menu_view, name='menu'),
    path('pedido/', realizar_pedido_view, name='crear_pedido'), # www.burgerqueen.com/menu/pedido/
    path('producto/<int:pk>/', detalle_producto_view, name='detalle_producto'), # www.burgerqueen.com/pedidos/producto/1/
]