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

#Landing page when server runs.
def index(request):
    return render(request, 'dashboard.html') #Returns a dashboard.

def register(request):
    if request.method == "POST":#User to send info/save/insert info to server
        form = RegisterForm(request.POST) #Form for registering is sent to client
        if form.is_valid(): #If all the fields are correctly populated, the form can be saved.
            user = form.save() #Form saved
            login(request, user) #Logged in user authenticated
            return redirect('dashboard')  # Redirect after login to the dashboard
    else:
        form = RegisterForm()
    return render(request, 'FitFair/register.html', {'form': form}) #The form template is rendered inorder for the user to register following the logic above.

def login(request):
    return render(request, 'login.html') #Renders a login page provided the user provides the correct login details.

def log(request):
    return render(request, 'FitFair/log.html')

#Views for models allowing all CRUD operations
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']

#View for logging a meal.
@login_required
def log_meal(request):
    if request.method == 'POST': # User requests a form/user wants to log a meal(client - server)
        form = MealForm(request.POST) #log_meal form is opened. 
        if form.is_valid(): #If all the fields are valid, then the user can save the info.
            meal = form.save(commit=False)
            meal.user = request.user  # Associate meal with logged-in user
            meal.save()
            return redirect('meal_list')  # Redirect after logging a meal
    else:
        form = MealForm()

    return render(request, 'FitFair/log_meal.html', {'form': form})


#Views for dispalying the meals the user has logged for a particular day.
@login_required
def meal_list(request):
    selected_date = request.GET.get('date')  #shows all the calendar days. GET method is the client requesting info to be retrieved from the server in this case a calendar with days.
    #selected_meal_of_the_day = request.GET.get('meal_of_the_day')
    meals = Meal.objects.filter(user=request.user).order_by('-date') #Retrieve data from the database based on user.
    total_calories = 0
    
    if selected_date:#If date is selected, only meals for the specific day needs to show.
        meals = meals.filter(date__date=selected_date)#Filter meals based on selected date by user.
        #meals = meals.filter(meal_of_the_day__meal_of_the_day = selected_meal_of_the_day)
        total_calories = meals.aggregate(Sum('total_calories')).get('total_calories__sum', 0) #Allows 0 if there were no meals logged for that day.
        #total_calories = meals.aggregate(total=Sum((Sum('carbs')*4) + 
                                                           #(Sum('proteins')*4) + (Sum('fiber')*2) + (Sum('fats')*9)))

    return render(request, 'FitFair/meal_list.html', {'meals': meals, 'selected_date': selected_date, 'total_calories': total_calories})

#def total_calories(self):
        #return self.nutritionalproduct.aggregate(total=Sum((Sum('carbohydrates')*4) + 
                                                           #(Sum('proteins')*4) + (Sum('fiber')*2) + (Sum('fats')*9)))







# Create your views here.
