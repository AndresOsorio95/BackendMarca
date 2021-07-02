
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from proveedor_app.models import *
from proveedor_app.serializers import *


class ProveedorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Proveedor.objects.all().order_by('nombre')
    serializer_class = ProveedorSerializer

    def get_queryset(self):
        queryset = super(ProveedorViewSet, self).get_queryset()
        if self.action == self.get_short.__name__:
            queryset = queryset.only('uuid', 'tipo_identificacion', 'identificacion', 'nombre',
                                     'direccion', 'numero_telefonico', 'correo_electronico', 'descripcion')
        if self.action == self.get_lite.__name__:
            queryset = queryset.only(
                'uuid', 'nombre')
        return super().get_queryset()

    def get_serializer_class(self):
        serializer = {
            'create': SaveProveedorSerializer,
            'get_short': GetShortProveedorSerializer,
            'get_lite': GetLiteProveedorSerializer
        }
        if self.action in serializer:
            return serializer[self.action]

        return ProveedorSerializer

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
