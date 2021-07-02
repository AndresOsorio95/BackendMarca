from django.apps import AppConfig


class ProductoBodegaAppConfig(AppConfig):
    name = 'producto_bodega_app'
    verbose_name = 'Productos en bodega'

    def ready(self):
        try:
            import producto_bodega_app.signals.producto_bodega
        except ImportError:
            pass