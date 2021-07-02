from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models


class Seccion(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    icono = models.CharField(max_length=50, default='far fa-folder')
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
