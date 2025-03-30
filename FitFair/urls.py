from django.urls import path, include
from .views import register, log, log_meal, meal_list
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from rest_framework.routers import DefaultRouter
from .views import MealViewSet

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('register/', register, name='register'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='FitFair/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='FitFair/logout.html'), name='logout'),
    path('log/_meal/', views.log_meal, name='log_meal'),
    path('meal_list/', meal_list, name='meal_list'),

]

router = DefaultRouter()
router.register(r'meal', MealViewSet)

urlpatterns += [
    path('api/', include(router.urls)),
]