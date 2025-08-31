from django import forms
from .models import MealLog

class MealForm(forms.ModelForm):
    class Meta:
        model = MealLog
        fields = ["meal_type", "food_name", "calories", "protein", "carbs", "fats", "date"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }
