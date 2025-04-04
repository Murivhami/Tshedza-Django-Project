from django.urls import path, include
from .views import MealViewSet, register
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'meals', MealViewSet)

urlpatterns = [
    # Registration, Login, Logout
    path('register/', views.register, name='register'),  # Register view (API)
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout view

    # Meals (API view for meals)
    path('tracker/', include(router.urls)),  # You can add your meal-related views here
]

