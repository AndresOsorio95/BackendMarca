from uuid import uuid4
from django_paranoid.models import ParanoidModel
from django.db import models
from producto_bodega_app.models import ProductoBodega


talla_opciones = [
    ["0-2", "0-2"],
    ["2-4", "2-4"],
    ["6-8", "6-8"],
    ["10-12", "10-12"],
    ["14-16", "14-16"],
    ["XS", "XS"],
    ["S", "S"],
    ["M", "M"],
    ["L", "L"],
    ["XL", "XL"],
    ["XXL", "XXL"],
    ["XXXL", "XXXL"]
]

color_opciones = [
    ["#FFEC33", "AMARILLO"],
    ["#09619a", "AZUL"],
    ["#FF3333", "ROJO"],
    ["#FFFFFF", "BLANCO"],
    ["#000000", "NEGRO"],
    ["#349C18", "VERDE"],
    ["#0a2e47","AZUL MARCA"],
    ["#d9d8d8","GRIS MARCA"]
]

estado_opciones = [
    ["OK", "OK"],
    ["DF", "DEFECTUOSO"],
    ["PD", "PARCIALMENTE DAÑADO"],
    ["CD", "COMPLETAMENTE DAÑADO"],
    ["ND", "NO DECEADO"],
    ["NE", "NO ESPERADO"]
]

class ProductoBodegaDetalle(ParanoidModel):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    producto_bodega = models.ForeignKey(ProductoBodega, on_delete=models.PROTECT)
    talla = models.CharField(max_length=6, choices=talla_opciones)
    color = models.CharField(max_length=7,choices=color_opciones)
    estado = models.CharField(max_length=2,choices=estado_opciones)
    informacion = models.TextField()