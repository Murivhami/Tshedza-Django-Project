from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Meal
from .serializers import MealSerializer
from .forms import MealForm, RegisterForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect after login
    else:
        form = RegisterForm()
    return render(request, 'FitFair/register.html', {'form': form})

def custom_login(request):
    return render(request, 'login.html')

def log(request):
    return render(request, 'FitFair/log.html')

#Views for models

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

@login_required
def log_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user  # Associate meal with logged-in user
            meal.save()
            return redirect('meal_list')  # Redirect after logging a meal
    else:
        form = MealForm()

    return render(request, 'FitFair/log_meal.html', {'form': form})

@login_required
def meal_list(request):
    meals = Meal.objects.filter(user=request.user).order_by('-date')

    return render(request, 'FitFair/meal_list.html', {'meals': meals})






# Create your views here.
