from bodega_app.models import Bodega
from django.forms import ModelForm, Textarea


class BodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = (
            'nombre_corto', 'nombre', 'capacidad_maxima', 'direccion',
            'numero_telefonico', 'correo_electronico', 'descripcion'
        )
        widgets = {
            'descripcion': Textarea(attrs={'cols': 40, 'rows': 6}),
        }
