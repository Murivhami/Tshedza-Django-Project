from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer, MealSerializer
from rest_framework import viewsets
from rest_framework import permissions

User = get_user_model()
#User registration view
class UserRegistrationView(APIView):
    def post(self, request):
        # Serialize the request data for creating a new user
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the user in the database
            # Generate a token for the new user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#User login view
from rest_framework.authtoken.views import obtain_auth_token
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        # This view uses the standard token authentication view provided by DRF
        return obtain_auth_token(request=request)

#User profile view
class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access

    def get(self, request):
        # Return the user's profile (using the custom user model)
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        # Update user profile information
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save updated user data
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
#Views for models allowing all CRUD operations
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]
    
     def perform_create(self, serializer):
        # Ensure that the meal is associated with the logged-in user
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        # Limit meals to only those belonging to the logged-in user
        return Meal.objects.filter(user=self.request.user)



