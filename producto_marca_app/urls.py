from rest_framework.routers import DefaultRouter
from producto_marca_app.views import ProductoMarcaViewSet

router = DefaultRouter()
router.register(r'product-marca', ProductoMarcaViewSet, basename='product-marca')
urlpatterns = router.urls
