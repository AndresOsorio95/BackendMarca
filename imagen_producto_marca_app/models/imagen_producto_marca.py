from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models
from producto_marca_app.models import ProductoMarca


class ImagenProductoMarca(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    producto_marca = models.ForeignKey(ProductoMarca, on_delete=models.PROTECT)
    imagen = models.ImageField()
    primera = models.BooleanField(default=False)
