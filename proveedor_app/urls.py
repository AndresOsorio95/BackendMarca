from rest_framework.routers import DefaultRouter
from proveedor_app.views import *

router = DefaultRouter()
router.register(r'provider', ProveedorViewSet, basename='provider')
urlpatterns = router.urls
