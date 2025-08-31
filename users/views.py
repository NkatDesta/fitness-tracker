from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from workouts.models import WorkoutLog
from nutrition.models import MealLog
from django.http import HttpResponseRedirect

# Home
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "home.html")

# Dashboard
@login_required
def dashboard(request):
    workouts = WorkoutLog.objects.filter(user=request.user)
    meals = MealLog.objects.filter(user=request.user)
    return render(request, "dashboard.html", {"workouts": workouts, "meals": meals})

# Login
def login_template_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return HttpResponseRedirect('/users/dashboard/')  # Make sure session is fully saved
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

# Register
def register_template_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, "Account created successfully")
            return HttpResponseRedirect('/users/dashboard/')
    return render(request, "register.html")

# Logout
def logout_view(request):
    logout(request)
    messages.success(request, "You’ve logged out successfully.")
    return redirect('home')
