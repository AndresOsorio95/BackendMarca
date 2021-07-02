from rest_framework.routers import DefaultRouter
from seccion_app.views import SeccionViewSet

router = DefaultRouter()
router.register(r'section', SeccionViewSet, basename='section')
urlpatterns = router.urls
