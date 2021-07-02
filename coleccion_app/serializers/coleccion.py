from django.db.models import fields
from rest_framework import serializers
from coleccion_app.models import Coleccion


class ColeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coleccion
        fields = '__all__'
        read_only_fields = ['uuid']


class GetShortColeccionSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    nombre = serializers.CharField()
    icono = serializers.CharField()
    descripcion = serializers.CharField()


class GetLiteColeccionSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    nombre = serializers.CharField()
    icono = serializers.CharField()


class SaveColeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coleccion
        fields = ["nombre", "icono", "descripcion"]

    def validate(self, attrs):
        attrs.update({
            'nombre': attrs.get('nombre').upper(),
        })
        return attrs
