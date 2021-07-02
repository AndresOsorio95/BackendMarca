from django.forms import ModelForm, widgets
from django.forms.fields import CharField
from django.forms import *


class ReporteBodegaForm(Form):
    date_range = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off',
        'name': 'date'
    }))
