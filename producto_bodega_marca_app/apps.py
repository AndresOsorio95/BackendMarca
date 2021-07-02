from django.apps import AppConfig


class ProductoBodegaMarcaAppConfig(AppConfig):
    name = 'producto_bodega_marca_app'
    verbose_name = 'Relacion Producto(Bodega - Marca)'

    def ready(self):
        try:
            import producto_bodega_marca_app.signals.producto_bodega_marca
        except ImportError:
            pass
