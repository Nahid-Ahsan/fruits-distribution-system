from django.urls import path
from . import views

urlpatterns = [
    path('prediction/', views.result, name='result'),
    
]


# api: http://127.0.0.1:8000/prediction/