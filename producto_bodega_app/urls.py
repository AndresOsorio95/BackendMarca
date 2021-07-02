
from rest_framework.routers import DefaultRouter
from producto_bodega_app.views import ProductoBodegaViewSet

router = DefaultRouter()
router.register(r'product-cellar', ProductoBodegaViewSet, basename='product-cellar')
urlpatterns = router.urls