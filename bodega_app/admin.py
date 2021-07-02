from bodega_app import serializers
from django.contrib import admin
from .models import Bodega
from .serializers import BodegaSerializer, SaveBodegaSerializer


class BodegaAdmin(admin.ModelAdmin):
    list_display = ["nombre_corto", "nombre", "capacidad_maxima",
                    "capacidad_disponible", "direccion", "numero_telefonico", "correo_electronico"]
    search_fields = ["uuid", "nombre_corto", "nombre", "capacidad_maxima",
                     "capacidad_disponible", "direccion", "numero_telefonico", "correo_electronico", "descripcion"]
    list_filter = ["nombre"]
    list_per_page = 5
    serializer_class = BodegaSerializer

    def get_serializer_class(self):
        serializer = {
            'create': SaveBodegaSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return BodegaSerializer


admin.site.register(Bodega, BodegaAdmin)
