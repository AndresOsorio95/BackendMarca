from django import forms
from django.forms import fields
from seccion_app.models import Seccion


class SeccionForm(forms.ModelForm):
    class Meta:
        model = Seccion
        fields = ["nombre", "icono", "descripcion"]
