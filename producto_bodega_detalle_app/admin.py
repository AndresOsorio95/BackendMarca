
from django.contrib import admin
from .models import ProductoBodegaDetalle


class ProductoBodegaDetalleAdmin(admin.ModelAdmin):
    list_display = ["producto_bodega", "talla", "color", "estado"]
    list_filter = ["producto_bodega", "talla", "color", "estado"]
    search_fields = ["producto_bodega", "talla",
                     "color", "estado", "informacion"]
    list_per_page = 10


admin.site.register(ProductoBodegaDetalle, ProductoBodegaDetalleAdmin)
