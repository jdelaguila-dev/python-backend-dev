from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto', 'nombre_cliente', 'direccion']
        # Tip Pro: Widgets para que se vea bonito con Bootstrap
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Cliente'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección de Entrega', 'rows': 3}),
        }