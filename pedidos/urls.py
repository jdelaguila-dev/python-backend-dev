from django.urls import path
from .views import (
    crear_producto,
    dashboard,
    menu_view,
    realizar_pedido_view,
    detalle_producto_view,
    registro,
)


urlpatterns = [
    # Ruta vacía '' significa: www.burgerqueen.com/pedidos/
    path("", menu_view, name="menu"),
    # www.burgerqueen.com/menu/pedido/
    path("pedido/", realizar_pedido_view, name="crear_pedido"),
    # www.burgerqueen.com/pedidos/producto/1/
    path("producto/<int:pk>/", detalle_producto_view, name="detalle_producto"),
    # www.burgerqueen.com/pedidos/producto/nuevo/
    path("producto/nuevo/", crear_producto, name="crear_producto"),
    # www.burgerqueen.com/pedidos/dashboard/
    path("dashboard/", dashboard, name="dashboard"),
    # www.burgerqueen.com/pedidos/registro/
    path("registro/", registro, name="registro"),
]
