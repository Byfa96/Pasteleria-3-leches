from rest_framework import serializers
from apps.shop.models import Pastel

class PastelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastel
        fields = '__all__'
        