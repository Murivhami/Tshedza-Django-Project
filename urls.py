from django.urls import path, include, admin
from rest_framework.routers import DefaultRouter
from FitFair.views import MealViewSet, CustomUserViewSet

router = DefaultRouter()
router.register(r'meal', MealViewSet)
router.register(r'users', CustomUserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]