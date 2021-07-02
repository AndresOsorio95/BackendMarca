from django.db.models import fields
from rest_framework import serializers
from proveedor_app.models import Proveedor


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
        read_only_fields = ['uuid']


class GetShortProveedorSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    identificacion = serializers.UUIDField()
    tipo_identificacion = serializers.CharField()
    nombre = serializers.CharField()
    direccion = serializers.CharField()
    numero_telefonico = serializers.CharField()
    correo_electronico = serializers.EmailField()
    descripcion = serializers.CharField()


class GetLiteProveedorSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    nombre = serializers.CharField()


class SaveProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ["tipo_identificacion", "identificacion", "nombre",
                  "direccion", "numero_telefonico", "correo_electronico", "descripcion"]

    def validate(self, attrs):
        attrs.update({
            'nombre': attrs.get('nombre').upper()
        })
        return attrs
