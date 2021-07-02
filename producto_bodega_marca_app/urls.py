from rest_framework.routers import DefaultRouter
from producto_bodega_marca_app.views import ProductoBodegaMarcaViewSet

router = DefaultRouter()
router.register(r'product-cellar-marca',
                ProductoBodegaMarcaViewSet, basename='product-cellar-marca')
urlpatterns = router.urls
