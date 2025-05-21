from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PastelViewSet, PruebaViewSet
from . import views

router = DefaultRouter()
router.register(r'pasteles', PastelViewSet)
router.register(r'pruebas', PruebaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pruebacrud/', views.prueba_create, name='pruebacreate'),
    path('pruebacrud/<int:pk>/editar/', views.prueba_update, name='prueba_update'),
    path('pruebacrud/<int:pk>/eliminar/', views.prueba_delete, name='prueba_delete'),
]