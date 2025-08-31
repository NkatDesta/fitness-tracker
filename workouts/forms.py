from django import forms
from .models import WorkoutLog

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutLog
        fields = [
            "exercise_name", "workout_type", "duration_minutes",
            "distance", "reps", "sets", "calories_burned", "date"
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
