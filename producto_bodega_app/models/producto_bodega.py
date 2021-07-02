from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models
from bodega_app.models import *
from proveedor_app.models import *

class ProductoBodega(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    bodega = models.ForeignKey(Bodega, on_delete=models.PROTECT)  
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)  
    referencia = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)  
    costo = models.DecimalField(default=0, decimal_places=2, max_digits=12)  
    costo_unitario = models.DecimalField(default=0, decimal_places=2, max_digits=12)  
    cantidad_entra = models.PositiveIntegerField(default=0)  
    cantidad_disponible = models.PositiveIntegerField(default=0)
    cantidad_minima = models.PositiveIntegerField(default=0)
    descripcion =  models.TextField() 
    is_relacionado = models.BooleanField(default=False)  

    def __str__(self):
        return (self.referencia + " - " + self.nombre)