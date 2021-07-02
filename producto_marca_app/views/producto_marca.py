from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from producto_marca_app.models import ProductoMarca
from producto_marca_app.serializers import ProductoMarcaSerializer, GetLiteProductoMarcaSerializer, GetShortProductoMarcaSerializer, SaveProductoMarcaSerializer


class ProductoMarcaViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ProductoMarca.objects.all().order_by('seccion', 'coleccion', 'nombre')
    serializer_class = ProductoMarcaSerializer

    def get_queryset(self):
        queryset = super(ProductoMarcaViewSet, self).get_queryset()
        if self.action == self.get_short.__name__:
            queryset = queryset.only('uuid', 'coleccion', 'seccion', 'referencia', 'nombre', 'costo', 'precio', 'utilidad',
                                     'descuento', 'unidad_minima_descuento', 'descripcion').order_by('seccion', 'coleccion', 'nombre')
        if self.action == self.get_lite.__name__:
            queryset = queryset.only('uuid', 'coleccion', 'seccion', 'referencia', 'nombre', 'precio', 'descuento', 'unidad_minima_descuento').order_by(
                'seccion', 'coleccion', 'nombre')
        return super().get_queryset()

    def get_serializer_class(self):
        serializer = {
            'create': SaveProductoMarcaSerializer,
            'get_short': GetShortProductoMarcaSerializer,
            'get_lite': GetLiteProductoMarcaSerializer
        }        
        if self.action in serializer:
            return serializer[self.action]
        return ProductoMarcaSerializer

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
