from rest_framework import serializers
from .models import WorkoutLog

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = '__all__'
        read_only_fields = ['user']
