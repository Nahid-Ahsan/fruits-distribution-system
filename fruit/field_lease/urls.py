from django.urls import path
from . import views
from rest_framework.authtoken import views as v

urlpatterns = [

    path('field-list/', views.field_list, name='field-list'),
    path('field-detail/<int:field_id>', views.field_detail, name='field-detail'),
    path('book-field/<int:field_id>', views.book_field, name='book-field'), 
    path('api-token-auth/',v.obtain_auth_token,name='api-token-auth')
]
