from django.forms import ModelForm, Textarea
from proveedor_app.models import Proveedor


class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = (
            'tipo_identificacion', 'identificacion', 'nombre',
            'direccion', 'numero_telefonico', 'correo_electronico', 'descripcion'
        )
        widgets = {
            'descripcion': Textarea(attrs={'cols': 40, 'rows': 6}),
        }
