from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator


from ..forms import PedidoForm, ProductoForm
from ..models import Producto, Categoria
from django.db.models import Q  # Importar Q para búsquedas avanzadas (OR)


# Función de comprobación: ¿Es miembro del staff?
def es_admin(user):
    return user.is_authenticated and user.is_staff


def menu_view(request):
    # 1. Empezamos trayendo TODOS los productos
    productos = Producto.objects.all()

    # 2. Capturamos los parámetros de la URL (Query Params)
    # Ejemplo: Si la URL es /menu/?q=hamburguesa&cat=2
    busqueda = request.GET.get("q")  # Captura el texto del buscador
    categoria_id = request.GET.get("cat")  # Captura el filtro de categoría

    # 3. Lógica del Buscador (Texto)
    if busqueda:
        # Usamos Q para decir: "Nombre contiene X" O "Descripción contiene X"
        productos = productos.filter(
            Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda)
        )

    # 4. Lógica del Filtro (Categoría)
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    # Traemos las categorías para llenar el <select> del filtro
    categorias = Categoria.objects.all()

    # 5. Configurar Paginacion
    # Mostrar 10 productos por página
    paginator = Paginator(productos, 6)
    # Obtener el número de página de los parámetros de la URL
    page_number = request.GET.get("page")
    # Obtener los productos de la página solicitada
    page_obj = paginator.get_page(page_number)

    # Renderizar la plantilla HTML
    # Es el "carrito" donde enviamos los datos al HTML
    context = {
        "productos": page_obj,  # Enviamos los productos paginados
        "categorias": categorias,  # Enviamos categorías al template
    }
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
@user_passes_test(es_admin)  # <--- Solo el admin puede crear productos
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
@user_passes_test(es_admin)  # <--- Solo el admin puede ver el dashboard
def dashboard(request):
    productos = Producto.objects.all()
    return render(request, "dashboard.html", {"productos": productos})


# Vista para registro de usaurios
def registro(request):
    if request.method == "POST":
        # UserCreationForm se encarga de:
        # 1. Validar que las contraseñas coincidan.
        # 2. Validar que el usuario no exista.
        # 3. Aplicar el algoritmo de Hashing (PBKDF2) antes de guardar.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # UX: Logueamos al usuario automáticamente tras registrarse
            # Esto crea la "Session ID" en la base de datos y en la cookie del navegador.
            login(request, usuario)
            return redirect("menu")
    else:
        form = UserCreationForm()
    return render(request, "registration/registro.html", {"form": form})
