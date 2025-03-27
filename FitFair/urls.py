from django.urls import path
from FitFair.views import register
from django.contrib.auth.views import LoginView 
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='FitFair/login.html'), name='login'),


]