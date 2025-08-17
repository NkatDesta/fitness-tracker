from django.urls import path
from .views import MealListCreateView, MealDetailView

urlpatterns = [
    path('meals/', MealListCreateView.as_view(), name='meal-list'),
    path('meals/<int:pk>/', MealDetailView.as_view(), name='meal-detail'),
]
