from rest_framework.routers import DefaultRouter
from producto_bodega_detalle_app.views import ProductoBodegaDetalleViewSet

router = DefaultRouter()
router.register(r'product-cellar-detail',
                ProductoBodegaDetalleViewSet, basename='product-cellar-detail')
urlpatterns = router.urls
