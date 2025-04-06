from rest_framework import serializers
from .models import Meal
from django.contrib.auth import get_user_model

User = get_user_model()

#Meal serializer
class MealSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Meal
        fields = '__all__'
        read_only_fields = ['username']
        

#CustomUser serializer
class CustomUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'location']

    def validate(self, data):
        # Check if the passwords match.
        if data['password1'] != data['password2']:
            #If the password does not match, an error is returned.
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