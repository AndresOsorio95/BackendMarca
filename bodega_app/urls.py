from rest_framework.routers import DefaultRouter
from bodega_app.views import *

router = DefaultRouter()
router.register(r'cellar', BodegaViewSet, basename='cellar')
urlpatterns = router.urls

