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
