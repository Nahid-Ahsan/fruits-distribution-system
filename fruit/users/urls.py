from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]



# apis: 

# http://127.0.0.1:8000/login/
# http://127.0.0.1:8000/signup/
# http://127.0.0.1:8000/logout/
