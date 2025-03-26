from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from FitFair.views import MealViewSet, MealTypeViewSet, NutritionalProductViewSet

router = DefaultRouter()
router.register(r'meals', MealViewSet)
router.register(r'meal-type', MealTypeViewSet)
router.register(r'nutritional_product', NutritionalProductViewSet)


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('FitFair/', include(router.urls)),
]
