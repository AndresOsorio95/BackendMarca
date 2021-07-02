from django.contrib import admin
from .models import ProductoBodega


class ProductoBodegaAdmin(admin.ModelAdmin):
    list_display = ["referencia", "nombre", "bodega", "proveedor",  "costo", "costo_unitario",
                    "cantidad_entra", "cantidad_disponible", "cantidad_minima"]
    list_filter = ["bodega", "proveedor"]
    search_fields = ["referencia", "nombre", "bodega", "proveedor",  "costo", "costo_unitario",
                     "cantidad_entra", "cantidad_disponible", "cantidad_minima", "descripcion"]
    list_per_page = 10


admin.site.register(ProductoBodega, ProductoBodegaAdmin)
