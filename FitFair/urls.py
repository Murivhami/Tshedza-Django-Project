from django.urls import path, include
from .views import APILoginView, MealViewSet, register
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # For obtaining access and refresh tokens
    TokenRefreshView,     # For refreshing access tokens
)


router = DefaultRouter()
router.register(r'meals', MealViewSet)

urlpatterns = [
    # Registration, Login, Logout
    path('register/', views.register, name='register'),  # Register view (API)
    path('login/', APILoginView.as_view(), name='api_login'),  # Login view
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout view

    # Meals (API view for meals)
    path('', include(router.urls)),  # You can add your meal-related views here
]

