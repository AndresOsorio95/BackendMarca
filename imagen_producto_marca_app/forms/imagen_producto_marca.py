from django import forms
from django.forms import widgets
from imagen_producto_marca_app.models import ImagenProductoMarca


class ImagenProductoMarcaForm(forms.ModelForm):
    class Meta:
        model = ImagenProductoMarca
        fields = ['imagen']
