
from django.apps import AppConfig


class ProductoBodegaDetalleAppConfig(AppConfig):
    name = 'producto_bodega_detalle_app'
    verbose_name = 'Productos en bodega detallado'

    def ready(self):
        try:
            import producto_bodega_detalle_app.signals.producto_bodega_detalle
        except ImportError:
            pass
