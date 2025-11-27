from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import PedidoForm, ProductoForm
from .models import Producto, Categoria, Pedido
from rest_framework import viewsets
from .serializers import ProductoSerializer, CategoriaSerializer, PedidoSerializer

# Decorador para proteger vistas que requieren login
from django.contrib.auth.decorators import login_required


def menu_view(request):
    # Consultar a la Base de Datos (ORM)
    # "Traeme todos los productos que existen"
    productos = Producto.objects.all()

    # Renderizar la plantilla HTML
    # Es el "carrito" donde enviamos los datos al HTML
    context = {"productos": productos}
    # Renderizar (Pintar) la plantilla
    return render(request, "menu.html", context)


def realizar_pedido_view(request):
    if request.method == "POST":
        # 1. El usuario envio datos
        form = PedidoForm(request.POST)

        if form.is_valid():
            # 2. Los datos son validos. Guardar en la Base de Datos
            form.save()

            # 3. Feedback al usuario (Gracias por su pedido)
            messages.success(
                request,
                "¡Gracias por su pedido! Tu pedido ha sido recibido correctamente.",
            )

            # 4. Redirigir al menú
            return redirect("menu")
    else:
        # 1. El usuario quiere ver el formulario (GET)
        form = PedidoForm()

    return render(request, "crear_pedido.html", {"form": form})


def detalle_producto_view(request, pk):
    # Si el producto no existe, devolver un error 404
    producto = get_object_or_404(Producto, pk=pk)

    # Creamos el contexto para enviar a la plantilla
    context = {"producto": producto}

    # Renderizamos la plantilla con el contexto
    return render(request, "detalle_producto.html", context)


# @login_required  # <--- Ahora nadie anónimo puede crear productos
@login_required
def crear_producto(request):
    if request.method == "POST":
        # request.POST trae el texto.
        # request.FILES trae las imágenes.
        # Si olvidan request.FILES, la foto nunca se guardará.
        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect("menu")
    else:
        form = ProductoForm()

    return render(request, "crear_producto.html", {"form": form})


# @login_required  # <--- Ahora nadie anónimo puede ver el dashboard
@login_required  # <--- EL GUARDIÁN: Si no estás logueado, te manda al login.
def dashboard(request):
    productos = Producto.objects.all()
    return render(request, "dashboard.html", {"productos": productos})


# ViewSet: ¡Hace la magia completa!
# Crea automáticamente la lógica para: Listar, Crear, Ver Detalle, Actualizar y Borrar.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
