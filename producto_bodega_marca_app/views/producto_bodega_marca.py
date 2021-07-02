from rest_framework import viewsets, mixins
from producto_bodega_marca_app.models import ProductoBodegaMarca
from producto_bodega_marca_app.serializers import ProductoBodegaMarcaSerializer, SaveProductoBodegaMarcaSerializer


class ProductoBodegaMarcaViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ProductoBodegaMarca.objects.all().order_by(
        'producto_marca', 'producto_bodega')
    serializer_class = ProductoBodegaMarcaSerializer

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductoBodegaMarcaSerializer
        }
        if self.action in serializer:

            return serializer[self.action]
        return ProductoBodegaMarcaSerializer
