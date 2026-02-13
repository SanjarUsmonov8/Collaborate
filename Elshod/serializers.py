from rest_framework import serializers
from .models import Elshod

class ElshodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elshod
        fields = '__all__'