from django.urls import path

from .views import home

urlpatterns = [
    path('', home, name='home'),  # URL para la vista de inicio
]