from rest_framework import serializers
from .models import Meal
from django.contrib.auth import get_user_model

User = get_user_model()

#Meal serializer
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'location']

    def validate(self, data):
        # Ensure passwords match
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        # Create the user with the validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password1'],
            age=validated_data.get('age'),
            location=validated_data.get('location'),
        )
        return user