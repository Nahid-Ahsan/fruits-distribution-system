# foodapp/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('fooditems/', views.FruitItemList.as_view(), name='food-item-list'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('fruitbook/<int:fruit_item_id>/', views.BookFruitView.as_view(), name='book-fruit')


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# api: 

# http://127.0.0.1:8000/categories/
# http://127.0.0.1:8000/fooditems/
# http://127.0.0.1:8000/fruitbook/1


"""
{
    "buyer": 2,  
    "fruit_requested": 5.5,
    "start_date": "2023-11-10",
    "contact_email": "buyer@example.com",
    "contact_phone": "1234567890"
}

"""