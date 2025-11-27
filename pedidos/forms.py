from django import forms
from .models import Pedido, Producto


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["producto", "nombre_cliente", "direccion"]
        # Tip Pro: Widgets para que se vea bonito con Bootstrap
        widgets = {
            "producto": forms.Select(attrs={"class": "form-select"}),
            "nombre_cliente": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del Cliente"}
            ),
            "direccion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Dirección de Entrega",
                    "rows": 3,
                }
            ),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "categoria", "descripcion", "imagen"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del Producto"}
            ),
            "precio": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Precio del Producto"}
            ),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Descripción del Producto",
                    "rows": 3,
                }
            ),
            # El input de archivo también se puede estilizar
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }
