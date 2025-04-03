from django import forms
from .models import Meal
#Registration Form

from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
#Allows user to register by filling in the fields.
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']  

class MealForm(forms.ModelForm):
#Allows users to log their meals and saves info into the database.
    class Meta:
        model = Meal
        fields = ['meal_of_the_day', 'food_item','fats', 'proteins', 'carbs' ,'quantity'] #'total_calories']



