from rest_framework import serializers
from .models import Category, fruitItem

class FruitItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = fruitItem
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
