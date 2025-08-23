from rest_framework import serializers
from .models import MealLog

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealLog
        fields = '__all__'
        read_only_fields = ['user']
