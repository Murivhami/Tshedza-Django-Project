from django import forms
from .models import Meal
#Registration Form

from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']  

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['meal_of_the_day', 'total_calories']



