from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from bodega_app.models import *
from bodega_app.serializers import *


class BodegaViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Bodega.objects.all().order_by('nombre')
    serializer_class = BodegaSerializer

    def get_queryset(self):
        queryset = super(BodegaViewSet, self).get_queryset()
        if self.action == self.get_short.__name__:
            queryset = queryset.only('uuid', 'nombre_corto', 'nombre', 'capacidad_maxima',
                                     'capacidad_disponible', 'direccion', 'numero_telefonico', 'correo_electronico', 'descripcion')
        if self.action == self.get_lite.__name__:
            queryset = queryset.only(
                'uuid', 'nombre_corto', 'nombre', 'capacidad_maxima', 'capacidad_disponible')
        return super().get_queryset()

    def get_serializer_class(self):
        serializer = {
            'create': SaveBodegaSerializer,
            'get_short': GetShortBodegaSerializer,
            'get_lite': GetLiteBodegaSerializer
        }
        if self.action in serializer:
            return serializer[self.action]

        return BodegaSerializer

    @action(methods=['GET'], detail=False, url_name='short', url_path='short', name='short')
    def get_short(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_name='lite', url_path='lite', name='lite')
    def get_lite(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
