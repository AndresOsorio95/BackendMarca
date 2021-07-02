from django.forms import ModelForm, Textarea
from producto_marca_app.models import ProductoMarca


class ProductoMarcaForm(ModelForm):
    class Meta:
        model = ProductoMarca
        fields = ('coleccion', 'seccion', 'nombre', 'descuento',
                  'unidad_minima_descuento', 'descripcion')
        widgets = {
            'descripcion': Textarea(attrs={'cols': 40, 'rows': 9}),
        }
