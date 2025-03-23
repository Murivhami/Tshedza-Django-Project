from rest_framework import serializers
from .models import CustomUser, MealType, Meal, NutritionalProduct

#serializer for CustomUsermodel
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

#serializer for Mealtype model
class MealTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealType
        fields = '__all__'

#serializer for meal model
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

#serializer for nutritionalproduct model.
class NutritionalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalProduct
        fields = '__all__'