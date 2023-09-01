from rest_framework import routers
from .views import BibliotecaViewSet

router = routers.DefaultRouter()
router.register(r'Biblioteca', BibliotecaViewSet)
urlpatterns = router.urls