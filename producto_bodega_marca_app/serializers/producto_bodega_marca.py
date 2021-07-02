from rest_framework import serializers
from producto_bodega_marca_app.models import ProductoBodegaMarca


class ProductoBodegaMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoBodegaMarca
        fields = '__all__'
        read_only_fields = ['uuid']


class GetShortProductoBodegaBodegaMarca(serializers.Serializer):
    uuid = serializers.UUIDField()
    cantidad = serializers.IntegerField()
    costo = serializers.FloatField()
    bodega = serializers.CharField()
    proveedor = serializers.CharField()
    referencia = serializers.CharField()
    nombre = serializers.CharField()
    cantidad_disponible = serializers.IntegerField()
    coleccion = serializers.CharField()
    seccion = serializers.CharField()
    nombre = serializers.CharField()
    costo = serializers.FloatField()
    precio = serializers.FloatField()
    descuento = serializers.IntegerField()
    unidad_minima_descuento = serializers.IntegerField()


class GetLiteProductoBodegaMarcaSerializer():
    uuid = serializers.UUIDField()
    producto_bodega = serializers.CharField()
    producto_marca = serializers.CharField()
    cantidad = serializers.IntegerField()
    costo = serializers.FloatField()


class SaveProductoBodegaMarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoBodegaMarca
        files = ['producto_bodega', 'producto_marca', 'cantidad']

    def validate(self, attrs):
        attrs.update({
            'costo': attrs.get('producto_bodega').costo_unitario * attrs.get('cantidad')
        })
        return attrs
