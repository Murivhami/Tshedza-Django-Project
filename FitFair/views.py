from django.contrib.auth.views import LoginView, LogoutView
#from .views import MealViewSet
from .serializers import MealSerializer, CustomUserSerializer
from .models import Meal
from rest_framework import viewsets, permissions, status
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
#from rest_framework.renderers import JSONRenderer
#from rest_framework.decorators import renderer_classes



#User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
#@renderer_classes([JSONRenderer]) 
def register(request):
    if request.method == 'POST':
        # Assume the request body contains the necessary data for registration
        serializer = CustomUserSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the user and return a response
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def create(self, validated_data):
    # Extract the fields needed for user creation
    username = validated_data['username']
    email = validated_data['email']
    password = validated_data['password1']
    age = validated_data.get('age', None)  # Optional fields
    location = validated_data.get('location', None)

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


#Views for models allowing all CRUD operations
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]
    
   # def perform_create(self, serializer):
        # Ensure that the meal is associated with the logged-in user
        #serializer.save(user=self.request.user)
    
    #def get_queryset(self):
        # Limit meals to only those belonging to the logged-in user
        #return Meal.objects.filter(user=self.request.user)

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
            return Response({'token': token.key})  # Send token as a response
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




