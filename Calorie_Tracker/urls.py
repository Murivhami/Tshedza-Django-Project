from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tracker/', include('FitFair.urls')),
      # Include the FitFair API URLs
]


