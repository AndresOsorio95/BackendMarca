from django.contrib import admin
from .models import Proveedor


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["tipo_identificacion", "identificacion", "nombre",
                    "direccion", "numero_telefonico", "correo_electronico"]
    search_fields = ["tipo_identificacion", "identificacion", "nombre",
                     "direccion", "numero_telefonico", "correo_electronico", "descripcion"]
    list_filter = ["tipo_identificacion"]
    list_per_page = 5


admin.site.register(Proveedor, ProveedorAdmin)
