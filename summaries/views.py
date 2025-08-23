from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from workouts.models import WorkoutLog
from nutrition.models import MealLog
from datetime import timedelta, date

class WeeklySummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        start_week = today - timedelta(days=7)

        workouts = WorkoutLog.objects.filter(user=request.user, date__gte=start_week)
        meals = MealLog.objects.filter(user=request.user, date__gte=start_week)

        total_duration = sum(w.duration_minutes for w in workouts)
        total_distance = sum(w.distance or 0 for w in workouts)
        total_workout_calories = sum(w.calories_burned for w in workouts)
        total_meal_calories = sum(m.calories for m in meals)

        return Response({
            "total_duration_minutes": total_duration,
            "total_distance": total_distance,
            "workout_calories_burned": total_workout_calories,
            "meal_calories_consumed": total_meal_calories,
            "net_calories": total_meal_calories - total_workout_calories
        })

