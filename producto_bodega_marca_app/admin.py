from django.contrib import admin
from .models import ProductoBodegaMarca


class ProductoBodegaMarcaAdmin(admin.ModelAdmin):
    list_display = ["producto_bodega", "producto_marca", "cantidad","costo"]
    search_fields = ["producto_bodega", "producto_marca", "cantidad","costo"]
    list_per_page = 10


admin.site.register(ProductoBodegaMarca, ProductoBodegaMarcaAdmin)