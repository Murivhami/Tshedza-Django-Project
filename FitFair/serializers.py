from rest_framework import serializers
from .models import CustomUser, Meal

User = get_user_model()

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['meal_of_the_day', 'total_calories', 'date']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
