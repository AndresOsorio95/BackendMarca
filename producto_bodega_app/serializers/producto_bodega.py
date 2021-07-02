from rest_framework import serializers
from producto_bodega_app.models import *
import random


class ProductoBodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoBodega
        fields = '__all__'
        read_only_fields = ['uuid']


class GetShortProductoBodegaSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    bodega = serializers.CharField()
    proveedor = serializers.CharField()
    referencia = serializers.CharField()
    nombre = serializers.CharField()
    costo = serializers.FloatField()
    costo_unitario = serializers.FloatField()
    cantidad_entra = serializers.IntegerField()
    cantidad_disponible = serializers.IntegerField()
    cantidad_minima = serializers.IntegerField()
    descripcion = serializers.CharField()
    is_relacionado = serializers.BooleanField()


class SaveProductoBodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoBodega
        fields = ['bodega', 'proveedor', 'nombre', 'costo',
                  'cantidad_entra', 'cantidad_minima', 'descripcion']

    def validate(self, attrs):
        if attrs.get('bodega').capacidad_disponible < attrs.get('cantidad_entra'):
            raise serializers.ValidationError({
                "status": "La cantidad ingresada excede la capacidad disponible de la bodega. "
            })
        bodega = attrs.get('bodega').nombre_corto
        nombre = attrs.get('nombre').upper()
        pre = nombre[0:4]
        rabd = random.randint(0, 9999)
        attrs.update({
            'nombre': nombre,
            'costo_unitario': attrs.get('costo') / attrs.get('cantidad_entra'),
            'referencia': bodega + "-" + pre + "-" + "{:0>3}".format(str(len(nombre))) + "-" + "{:0>4}".format(str(rabd))
        })
        return attrs
