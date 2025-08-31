from django.urls import path
from .views import workouts_template_view, add_workout_view

urlpatterns = [
    path("", workouts_template_view, name="workouts_template"),
    path("add/", add_workout_view, name="add_workout"),
]
