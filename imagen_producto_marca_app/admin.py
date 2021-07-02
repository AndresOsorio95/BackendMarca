from bodega_app import serializers
from django.contrib import admin
from .models import ImagenProductoMarca


class ImagenProductoMarcaAdmin(admin.ModelAdmin):
    list_display = ["uuid","producto_marca", "imagen"]
    list_per_page = 10


admin.site.register(ImagenProductoMarca, ImagenProductoMarcaAdmin)
