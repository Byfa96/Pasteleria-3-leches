from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PastelViewSet

router = DefaultRouter()
router.register(r'pasteles', PastelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]