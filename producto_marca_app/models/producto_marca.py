from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator
from django_paranoid.models import ParanoidModel
from django.db import models
from coleccion_app.models import Coleccion
from seccion_app.models import Seccion


class ProductoMarca(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.PROTECT)
    seccion = models.ForeignKey(Seccion, on_delete=models.PROTECT)
    referencia = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    costo = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    precio = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    utilidad = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    descuento = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    unidad_minima_descuento = models.IntegerField(default=0)
    descripcion = models.TextField()

    def __str__(self):
        return (self.referencia + " " + self.nombre)
