from django.db import models
from django.contrib.auth.models import User

class WorkoutLog(models.Model):
    WORKOUT_TYPES = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    distance = models.FloatField(null=True, blank=True)
    calories_burned = models.IntegerField()
    workout_type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    date = models.DateField()
