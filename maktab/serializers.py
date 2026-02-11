# serializers.py
from rest_framework import serializers
from .models import Maktab

class MaktabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maktab
        fields = '__all__'