from rest_framework.routers import DefaultRouter
from coleccion_app.views import ColeccionViewSet

router = DefaultRouter()
router.register(r'collection', ColeccionViewSet, basename='collection')
urlpatterns = router.urls
