from django.urls import path
from .views import WorkoutListCreateView, WorkoutDetailView

urlpatterns = [
    path('workouts/', WorkoutListCreateView.as_view(), name='workout-list'),
    path('workouts/<int:pk>/', WorkoutDetailView.as_view(), name='workout-detail'),
]
