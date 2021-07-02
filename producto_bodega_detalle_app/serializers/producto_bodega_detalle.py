from rest_framework import serializers
from producto_bodega_detalle_app.models import *


class ProductoBodegaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoBodegaDetalle
        fields = '__all__'
        read_only_fields = ['uuid']


class SaveProductoBodegaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoBodegaDetalle
        fields = ['producto_bodega', 'talla', 'color', 'estado', 'informacion']

    def validate(self, attrs):
        if attrs.get('producto_bodega').is_relacionado:
            raise serializers.ValidationError({
                "status": "El producto ya fue inventariado"
            })
        return attrs
