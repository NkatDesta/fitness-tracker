from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MealLog
from .forms import MealForm

@login_required
def meals_template_view(request):
    meals = MealLog.objects.filter(user=request.user).order_by("-date")
    return render(request, "nutrition.html", {"meals": meals})

@login_required
def add_meal_view(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect("meals_template")  # Redirect back to nutrition page
    else:
        form = MealForm()
    return render(request, "add_meal.html", {"form": form})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MealLog
from .forms import MealForm

@login_required
def nutrition_template_view(request):
    meals = MealLog.objects.filter(user=request.user).order_by("-date")
    return render(request, "nutrition.html", {"meals": meals})

@login_required
def add_meal_view(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect("nutrition_template")
    else:
        form = MealForm()
    return render(request, "add_meal.html", {"form": form})
