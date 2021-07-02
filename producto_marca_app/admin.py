from django.contrib import admin
from .models import ProductoMarca


class ProductoMarcaAdmin(admin.ModelAdmin):
    list_display = ["referencia", "nombre", "coleccion", "seccion", "costo",
                    "precio", "utilidad", "descuento", "unidad_minima_descuento"]
    search_fields = ["referencia", "nombre", "coleccion", "seccion", "costo",
                     "precio", "utilidad", "descuento", "unidad_minima_descuento", "descripcion"]
    search_fields = ["coleccion", "seccion"]
    list_per_page = 10


admin.site.register(ProductoMarca, ProductoMarcaAdmin)
