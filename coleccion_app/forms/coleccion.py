from django import forms
from django.forms import fields
from coleccion_app.models import Coleccion


class ColeccionForm(forms.ModelForm):
    class Meta:
        model = Coleccion
        fields = ["nombre", "icono", "descripcion"]
