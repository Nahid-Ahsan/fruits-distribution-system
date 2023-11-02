from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('homepage/', include('homepage.urls')),
    path('', include('users.urls')),
    path('', include('food.urls')),
    path('', include('fruitDisease.urls')),
    path('field/', include('fieldLease.urls')),
]
