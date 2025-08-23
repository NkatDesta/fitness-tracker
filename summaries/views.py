from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from workouts.models import WorkoutLog
from nutrition.models import MealLog
from collections import defaultdict
from datetime import timedelta, date

class WeeklySummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        start_week = today - timedelta(days=7)

        workouts = WorkoutLog.objects.filter(user=request.user, date__gte=start_week)
        meals = MealLog.objects.filter(user=request.user, date__gte=start_week)

        daily_summary = defaultdict(lambda: {"workout_minutes": 0, "calories_burned": 0, "calories_eaten": 0})

        for w in workouts:
            daily_summary[w.date]["workout_minutes"] += w.duration_minutes
            daily_summary[w.date]["calories_burned"] += w.calories_burned

        for m in meals:
            daily_summary[m.date]["calories_eaten"] += m.calories

        return Response({
            "totals": {
                "total_minutes": sum(w.duration_minutes for w in workouts),
                "total_distance": sum(w.distance or 0 for w in workouts),
                "total_calories_burned": sum(w.calories_burned for w in workouts),
                "total_calories_eaten": sum(m.calories for m in meals),
            },
            "daily": daily_summary
        })
