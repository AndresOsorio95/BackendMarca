from django.db.models import F, Sum
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from producto_bodega_app.models import *
from producto_bodega_app.serializers import *


class ProductoBodegaViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ProductoBodega.objects.all()
    serializer_class = ProductoBodegaSerializer

    def get_queryset(self):
        queryset = super(ProductoBodegaViewSet, self).get_queryset()
        if self.action == self.get_short.__name__:
            queryset = queryset.only('uuid', 'bodega', 'proveedor', 'referencia', 'nombre', 'costo', 'costo_unitario',
                                     'cantidad_entra', 'cantidad_disponible', 'cantidad_minima', 'descripcion', 'is_relacionado').order_by('nombre')
            
        return super().get_queryset()

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductoBodegaSerializer,
            'get_short': GetShortProductoBodegaSerializer
        }
        if self.action in serializer:
            return serializer[self.action]

        return ProductoBodegaSerializer

    @action(methods=['GET'], detail=False, url_name='short', url_path='short', name='short')
    def get_short(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
