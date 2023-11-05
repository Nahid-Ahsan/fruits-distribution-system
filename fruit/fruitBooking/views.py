from rest_framework import generics
from .models import Category, fruitItem, fruitBooking
from .serializers import CategorySerializer, FruitItemSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
 

class FruitItemList(generics.ListAPIView):
    queryset = fruitItem.objects.all()
    serializer_class = FruitItemSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookFruitView(APIView):
    def post(self, request, fruit_item_id):
        try:
            fruit_item = fruitItem.objects.get(id=fruit_item_id)
        except fruitItem.DoesNotExist:
            return Response({"error": "Fruit item not found"}, status=status.HTTP_404_NOT_FOUND)

        if fruit_item.seller == request.user:
            return Response({"error": "You can't book your own fruit item"}, status=status.HTTP_400_BAD_REQUEST)

        buyer_id = request.data.get("buyer")
        try:
            buyer = User.objects.get(id=buyer_id)
        except User.DoesNotExist:
            return Response({"error": "Buyer not found"}, status=status.HTTP_400_BAD_REQUEST)

        fruit_requested = request.data.get("fruit_requested")
        start_date = request.data.get("start_date")
        contact_email = request.data.get("contact_email")
        contact_phone = request.data.get("contact_phone")

        if not fruit_requested or not start_date or not contact_email or not contact_phone:
            return Response({"error": "Please provide all required information"}, status=status.HTTP_400_BAD_REQUEST)

        if fruit_requested > fruit_item.quantity:
            return Response({"error": "Not enough quantity available for booking"}, status=status.HTTP_400_BAD_REQUEST)

        booking = fruitBooking(
            fruit_name=fruit_item,
            buyer=buyer,
            seller=fruit_item.seller.username,  
            fruit_requested=fruit_requested,
            start_date=start_date,
            contact_email=contact_email,
            contact_phone=contact_phone,
        )

        booking.save()
        return Response({"message": "Booking successful"}, status=status.HTTP_201_CREATED)

