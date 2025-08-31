from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from workouts.models import WorkoutLog
from nutrition.models import MealLog

@login_required
def progress_view(request):
    # Workouts summary
    workouts = WorkoutLog.objects.filter(user=request.user)
    total_workouts = workouts.count()
    total_calories_burned = sum(w.calories_burned for w in workouts)

    # Nutrition summary
    meals = MealLog.objects.filter(user=request.user)
    total_calories_consumed = sum(m.calories for m in meals)

    context = {
        "total_workouts": total_workouts,
        "total_calories_burned": total_calories_burned,
        "total_calories_consumed": total_calories_consumed,
    }

    return render(request, "progress.html", context)
