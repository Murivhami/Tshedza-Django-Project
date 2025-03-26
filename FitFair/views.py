from .models import CustomUser, MealType, Meal, NutritionalProduct
from rest_framework import viewsets
from .serializers import CustomUserSerializer, MealSerializer, MealTypeSerializer, NutritionalProductSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealTypeViewSet(viewsets.ModelViewSet):
    queryset = MealType.objects.all()
    serializer_class = MealTypeSerializer

class NutritionalProductViewSet(viewsets.ModelViewSet):
    queryset = NutritionalProduct.objects.all()
    serializer_class = NutritionalProductSerializer




# Create your views here.
