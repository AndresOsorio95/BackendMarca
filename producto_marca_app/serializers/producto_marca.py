from rest_framework import serializers
from producto_marca_app.models import ProductoMarca
import random


class ProductoMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoMarca
        fields = '__all__'
        read_only_fields = ['uuid']


class GetShortProductoMarcaSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    coleccion = serializers.CharField()
    seccion = serializers.CharField()
    referencia = serializers.CharField()
    nombre = serializers.CharField()
    costo = serializers.FloatField()
    precio = serializers.FloatField()
    utilidad = serializers.FloatField()
    descuento = serializers.IntegerField()
    unidad_minima_descuento = serializers.IntegerField()
    descripcion = serializers.CharField()


class GetLiteProductoMarcaSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    coleccion = serializers.CharField()
    seccion = serializers.CharField()
    referencia = serializers.CharField()
    nombre = serializers.CharField()
    precio = serializers.FloatField()
    descuento = serializers.IntegerField()
    unidad_minima_descuento = serializers.IntegerField()


class SaveProductoMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoMarca
        fields = ['coleccion', 'seccion', 'nombre', 'descuento',
                  'unidad_minima_descuento', 'descripcion']

    def validate(self, attrs):
        nombre = attrs.get('nombre').upper()
        pre = nombre[0:4]
        rabd = random.randint(0, 9999)
        attrs.update({
            'nombre': nombre,
            'referencia': "-" + pre + "-" + "{:0>3}".format(str(len(nombre))) + "-" + "{:0>4}".format(str(rabd))
        })
        return attrs
