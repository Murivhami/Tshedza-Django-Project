from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer, MealSerializer
from rest_framework import viewsets
from rest_framework import permissions

#Creating a new User
class CreateUserView(APIView):
    def post(self, request):
        # Create a new user using the provided data
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This will save the new user to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Retrieve User
class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)  # Use dynamic user model here
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize the user object
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

#Update User
class UpdateUserView(APIView):
    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update the user with the new data
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Update the user in the database
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



