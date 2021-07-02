from django.db.models import fields
from rest_framework import serializers
from seccion_app.models import Seccion


class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'
        read_only_fields = ['uuid']


class GetShortSeccionSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    nombre = serializers.CharField()
    icono = serializers.CharField()
    descripcion = serializers.CharField()


class GetLiteSeccionSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    nombre = serializers.CharField()
    icono = serializers.CharField()


class SaveSeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = ["nombre", "icono", "descripcion"]

    def validate(self, attrs):
        attrs.update({
            'nombre': attrs.get('nombre').upper(),
        })
        return attrs
