from django import forms
from producto_bodega_marca_app.models import ProductoBodegaMarca


class ProductoBodegaMarcaForm(forms.ModelForm):
    class Meta:
        model = ProductoBodegaMarca
        fields = ["producto_bodega", "producto_marca", "cantidad"]
