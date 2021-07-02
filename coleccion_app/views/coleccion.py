from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from coleccion_app.models import *
from coleccion_app.serializers import *


class ColeccionViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Coleccion.objects.all().order_by('nombre')
    serializer_class = ColeccionSerializer

    def get_queryset(self):
        queryset = super(ColeccionViewSet, self).get_queryset()
        if self.action == self.get_short.__name__:
            queryset = queryset.only('uuid', 'nombre', 'icono', 'descripcion')
        if self.action == self.get_lite.__name__:
            queryset = queryset.only('uuid', 'nombre', 'icono')
        return super().get_queryset()

    def get_serializer_class(self):
        serializer = {
            'create': SaveColeccionSerializer,
            'get_short': GetShortColeccionSerializer,
            'get_lite': GetLiteColeccionSerializer
        }
        if self.action in serializer:
            return serializer[self.action]

        return ColeccionSerializer

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
