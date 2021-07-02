from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models
from producto_bodega_app.models import ProductoBodega
from producto_marca_app.models import ProductoMarca, producto_marca


class ProductoBodegaMarca(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    producto_bodega = models.ForeignKey(
        ProductoBodega, on_delete=models.PROTECT)
    producto_marca = models.ForeignKey(ProductoMarca, on_delete=models.PROTECT)
    cantidad = models.PositiveBigIntegerField(default=1)
    costo = models.DecimalField(default=0, decimal_places=2, max_digits=12)

