from django import forms
from producto_bodega_detalle_app.models import ProductoBodegaDetalle


class ProductoBodegaDetalleForm(forms.ModelForm):
    class Meta:
        model = ProductoBodegaDetalle
        fields = ["talla", "color", "estado", "informacion"]
