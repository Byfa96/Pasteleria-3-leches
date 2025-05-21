from rest_framework import serializers
from apps.shop.models import Pastel
from .models import Prueba

class PastelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastel
        fields = '__all__'
        
class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = '__all__'