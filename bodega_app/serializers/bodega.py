
from rest_framework import serializers
from bodega_app.models import Bodega


class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = '__all__'
        read_only_fields = ['uuid']


class GetShortBodegaSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    nombre_corto = serializers.CharField()
    nombre = serializers.CharField()
    capacidad_maxima = serializers.IntegerField()
    capacidad_disponible = serializers.IntegerField()
    direccion = serializers.CharField()
    numero_telefonico = serializers.CharField()
    correo_electronico = serializers.EmailField()
    descripcion = serializers.CharField()


class GetLiteBodegaSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    nombre_corto = serializers.CharField()
    nombre = serializers.CharField()
    capacidad_maxima = serializers.IntegerField()
    capacidad_disponible = serializers.IntegerField()


class SaveBodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        fields = ["nombre_corto", "nombre", "capacidad_maxima", "direccion",
                  "numero_telefonico", "correo_electronico", "descripcion"]

    def validate(self, attrs):
        attrs.update({
            'nombre_corto': attrs.get('nombre_corto').upper(),
            'nombre': attrs.get('nombre').upper(),
            'capacidad_disponible': attrs.get('capacidad_maxima')
        })
        return attrs
