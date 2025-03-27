from django.urls import path
from FitFair.views import register

urlpatterns = [
    path('register/', register, name='register'),

]