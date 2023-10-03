# foodapp/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('fooditems/', views.FoodItemList.as_view(), name='food-item-list'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('fooditems/<int:category_id>/', views.FoodItemListByCategory.as_view(), name='food-item-list-by-category'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
