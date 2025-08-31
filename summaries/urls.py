from django.urls import path
from .views import progress_view

urlpatterns = [
    path('progress/', progress_view, name='progress_template'), 
]
