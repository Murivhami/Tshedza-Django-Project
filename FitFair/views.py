from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Meal
from .serializers import MealSerializer
from .forms import MealForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum


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

def login(request):
    return render(request, 'login.html')

def log(request):
    return render(request, 'FitFair/log.html')

#Views for models

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']

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
    selected_date = request.GET.get('date')
    #selected_meal_of_the_day = request.GET.get('meal_of_the_day')
    meals = Meal.objects.filter(user=request.user).order_by('-date')
    total_calories = 0
    
    if selected_date:#If date is selected, only meals for the specific day needs to show.
        meals = meals.filter(date__date=selected_date)#Filter meals based on selected date by user.
        #meals = meals.filter(meal_of_the_day__meal_of_the_day = selected_meal_of_the_day)
        total_calories = meals.aggregate(Sum('total_calories')).get('total_calories__sum', 0)
        #total_calories = meals.aggregate(total=Sum((Sum('carbs')*4) + 
                                                           #(Sum('proteins')*4) + (Sum('fiber')*2) + (Sum('fats')*9)))

    return render(request, 'FitFair/meal_list.html', {'meals': meals, 'selected_date': selected_date, 'total_calories': total_calories})

#def total_calories(self):
        #return self.nutritionalproduct.aggregate(total=Sum((Sum('carbohydrates')*4) + 
                                                           #(Sum('proteins')*4) + (Sum('fiber')*2) + (Sum('fats')*9)))







# Create your views here.
