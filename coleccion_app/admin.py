from django.contrib import admin
from .models import Coleccion


class ColeccionAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]
    search_fields = ["nombre", "descripcion"]
    list_per_page = 5


admin.site.register(Coleccion, ColeccionAdmin)
