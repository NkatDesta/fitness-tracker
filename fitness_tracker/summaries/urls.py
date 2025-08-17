from django.urls import path
from .views import WeeklySummaryView

urlpatterns = [
    path('summary/weekly/', WeeklySummaryView.as_view(), name='weekly-summary'),
]
