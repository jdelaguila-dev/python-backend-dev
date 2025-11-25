from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import PedidoForm
from .models import Producto

def menu_view(request):
    # Consultar a la Base de Datos (ORM)
    # "Traeme todos los productos que existen"
    productos = Producto.objects.all()
    
    # Renderizar la plantilla HTML
    # Es el "carrito" donde enviamos los datos al HTML
    context = {
        'productos': productos
    }
    # Renderizar (Pintar) la plantilla
    return render(request, 'menu.html', context)


def realizar_pedido_view(request):
    if request.method == 'POST':
        # 1. El usuario envio datos
        form = PedidoForm(request.POST)
        
        if form.is_valid():
            # 2. Los datos son validos. Guardar en la Base de Datos
            form.save()
            
            # 3. Feedback al usuario (Gracias por su pedido)
            messages.success(
                request, 
                '¡Gracias por su pedido! Tu pedido ha sido recibido correctamente.'
            )
            
            # 4. Redirigir al menú
            return redirect('menu')
    else:
        # 1. El usuario quiere ver el formulario (GET)
        form = PedidoForm()
        
    return render(request, 'crear_pedido.html', {'form': form})

def detalle_producto_view(request, pk):
    # Si el producto no existe, devolver un error 404
    producto = get_object_or_404(Producto, pk=pk)
    
    # Creamos el contexto para enviar a la plantilla
    context = {
        'producto': producto
    }
    
    # Renderizamos la plantilla con el contexto
    return render(request, 'detalle_producto.html', context)