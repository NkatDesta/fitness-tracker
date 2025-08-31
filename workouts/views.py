from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WorkoutLog
from .forms import WorkoutForm

@login_required
def workouts_template_view(request):
    workouts = WorkoutLog.objects.filter(user=request.user).order_by("-date")
    
    # Group workouts by type
    workouts_by_type = {
        "Cardio": workouts.filter(workout_type="cardio"),
        "Strength": workouts.filter(workout_type="strength"),
        "Flexibility": workouts.filter(workout_type="flexibility"),
    }
    
    return render(request, "workouts.html", {"workouts_by_type": workouts_by_type})


@login_required
def add_workout_view(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect("workouts_template")
    else:
        form = WorkoutForm()
    return render(request, "add_workout.html", {"form": form})
