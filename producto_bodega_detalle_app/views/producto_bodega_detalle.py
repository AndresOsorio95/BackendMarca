from rest_framework import viewsets, mixins
from producto_bodega_detalle_app.models import *
from producto_bodega_detalle_app.serializers import *


class ProductoBodegaDetalleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ProductoBodegaDetalle.objects.all().order_by(
        'producto_bodega', 'estado', 'talla', 'color')
    serializer_class = ProductoBodegaDetalleSerializer

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductoBodegaDetalleSerializer
        }
        if self.action in serializer:
            return serializer[self.action]
        return ProductoBodegaDetalleSerializer
