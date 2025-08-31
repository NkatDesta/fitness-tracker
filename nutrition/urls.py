from django.urls import path
from .views import nutrition_template_view, add_meal_view

urlpatterns = [
    path("", nutrition_template_view, name="nutrition_template"),
    path("add/", add_meal_view, name="add_meal"),
]
