from django.shortcuts import render
from .serializers import MealSerializer, CustomUserSerializer
from .models import Meal
from rest_framework import viewsets, permissions, status
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime, date


#App landing page
def index(request):
    return render(request, 'dashboard.html') #Returns a dashboard.


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        # Becomes succesfull and the request body has all the required details for registering a user.
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the registered user and return a response to confirm sucessful registration.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #Returns error is the registration was not successful.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def create(self, validated_data):
    # Extract the fields required for new user creation.
    username = validated_data['username']
    email = validated_data['email']
    password = validated_data['password1']
    age = validated_data.get('age', None)  # A user can still be created even if this field is not provided.
    location = validated_data.get('location', None) # A user can still be created even if this field is not provided.

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
    )

    # Save additional fields if present
    if age:
        user.age = age
    if location:
        user.location = location
    user.save()

    return user


#Views for meal model allowing all CRUD operations
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

#Retrive meals belonging to a user.
    def get_queryset(self):
      user = self.request.user
      #return Meal.objects.all()
      return Meal.objects.filter(user=self.request.user)

#Filtering the meal info based on the date
    def get_queryset(self):
        queryset = Meal.objects.filter(user=self.request.user)
        
        # Get the date filter from the query parameters
        date_filter = self.request.query_params.get('date', None)
        
        if date_filter:
            # If a date is provided, filter meals by the date
            try:
                date = datetime.strptime(date_filter, '%Y-%m-%d').date()
                queryset = queryset.filter(date=date)
            except ValueError:
                pass  
        return queryset
    
    def perform_create(self, serializer):
        # Ensure that the meal belongs to the logged in user.
        serializer.save(user=self.request.user)
        #Meal of the day filter

    def get_queryset(self):
        queryset = Meal.objects.filter(user=self.request.user)
        meal_type = self.request.query_params.get('meal_of_the_day', None)
        if meal_type:
            # If the meal type is provided, filter meals by the meal of the day(breakfast,lunch and dinner)
                queryset = queryset.filter(meal_of_the_day=meal_type)
        return queryset 


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny

class APILoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        print(f"Username: {username}, Password: {password}")

        # Authenticate user using email and password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate a token for the authenticated user
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})  # When the user in the database and the login is successful, 
        #a token is sent in response.
        else:
            #If the user credentials are not valid or the user does not exist on the system.
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




