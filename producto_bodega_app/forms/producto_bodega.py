from django.forms import ModelForm, Textarea
from producto_bodega_app.models import ProductoBodega


class ProductoBodegaForm(ModelForm):
    class Meta:
        model = ProductoBodega
        fields = ('bodega', 'proveedor', 'nombre', 'costo',
                  'cantidad_entra', 'cantidad_minima', 'descripcion')
        widgets = {
            'descripcion': Textarea(attrs={'cols': 40, 'rows': 6}),
        }
