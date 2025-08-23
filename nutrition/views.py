from django.shortcuts import render
from rest_framework import generics, permissions
from .models import MealLog
from .serializers import MealSerializer

class MealListCreateView(generics.ListCreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MealLog.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MealDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MealLog.objects.filter(user=self.request.user)

