from rest_framework import serializers
from .models import Meal, CustomUser

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['meal_of_the_day', 'total_calories', 'date']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'age', 'location']
