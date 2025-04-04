from rest_framework import serializers
from .models import Meal
from django.contrib.auth import get_user_model

User = get_user_model()

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['meal_of_the_day', 'total_calories', 'date']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'location']
