from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models

tipo_identificacion_opciones = [
    ["C.C.", "CEDULA DE CIUDADANIA"],
    ["C.E.", "CEDULA DE EXTRANJERIA"],
    ["N.I.P.", "NUMERO DE IDENTIFICACION PERSONAL"],
    ["N.I.T.", "NUMERO DE IDENTIFICACION TRIBUTARIA"],
    ["T.I.", "TARJETA DE IDENTIDAD"],
    ["P.A.P.", "PASAPORTE"]
]


class Proveedor(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    tipo_identificacion = models.CharField(
        max_length=7, choices=tipo_identificacion_opciones)
    identificacion = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    numero_telefonico = models.CharField(max_length=10)
    correo_electronico = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
