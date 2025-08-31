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
    workout_type = models.CharField(max_length=20, choices=WORKOUT_TYPES)
    duration_minutes = models.PositiveIntegerField()
    distance = models.FloatField(null=True, blank=True)
    reps = models.PositiveIntegerField(null=True, blank=True)
    sets = models.PositiveIntegerField(null=True, blank=True)
    calories_burned = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.exercise_name} ({self.user.username})"
