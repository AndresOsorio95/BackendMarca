from django.contrib import admin
from .models import Seccion


class SeccionAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]
    search_fields = ["nombre", "descripcion"]
    list_per_page = 5


admin.site.register(Seccion, SeccionAdmin)
