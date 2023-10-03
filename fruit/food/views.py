from rest_framework import generics
from .models import Category, FoodItem
from .serializers import CategorySerializer, FoodItemSerializer

class FoodItemList(generics.ListAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FoodItemListByCategory(generics.ListAPIView):
    serializer_class = FoodItemSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return FoodItem.objects.filter(category_id=category_id)
