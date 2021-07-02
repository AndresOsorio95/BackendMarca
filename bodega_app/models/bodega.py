from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator
from django_paranoid.models import ParanoidModel
from django.db import models

class Bodega(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    nombre_corto = models.CharField(max_length=6)
    nombre = models.CharField(max_length=50)
    capacidad_maxima = models.PositiveIntegerField(default=0)
    capacidad_disponible = models.PositiveIntegerField(default=0)
    direccion= models.CharField(max_length=80)
    numero_telefonico = models.CharField(max_length=10)
    correo_electronico= models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return (self.nombre_corto + " - " + self.nombre)