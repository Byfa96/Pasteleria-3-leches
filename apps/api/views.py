from django.shortcuts import render
from rest_framework import viewsets
from apps.shop.models import Pastel
from .serializers import PastelSerializer

class PastelViewSet(viewsets.ModelViewSet):
    queryset = Pastel.objects.all()
    serializer_class = PastelSerializer