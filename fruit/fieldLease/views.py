from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Field, Booking
from .serializers import BookingSerializer
from django.contrib.auth.models import User
from .serializers import * 
from rest_framework import generics



class FieldList(generics.ListAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class BookFieldView(APIView):
    def post(self, request, field_id):
        
        try:
            field = Field.objects.get(id=field_id)
        except Field.DoesNotExist:
            return Response({"error": "Field not found"}, status=status.HTTP_404_NOT_FOUND)

        if field.owner == request.user:
            return Response({"error": "You can't book your own field"}, status=status.HTTP_400_BAD_REQUEST)

        print(field.owner)

        farmer_id = request.data.get("farmer")
        try:
            farmer = User.objects.get(id=farmer_id)
        except User.DoesNotExist:
            return Response({"error": "Farmer not found"}, status=status.HTTP_400_BAD_REQUEST)

        acres_requested = request.data.get("acres_requested")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        contact_email = request.data.get("contact_email")
        contact_phone = request.data.get("contact_phone")

        if not acres_requested or not start_date or not end_date or not contact_email or not contact_phone:
            return Response({"error": "Please provide all required information"}, status=status.HTTP_400_BAD_REQUEST)

        if acres_requested > field.size_in_acres:
            return Response({"error": "Not enough acres available for booking"}, status=status.HTTP_400_BAD_REQUEST)

       
        booking = Booking(
            fieldOwner=field,
            owner_name = field.owner,
            farmer=farmer,
            acres_requested=acres_requested,
            start_date=start_date,
            end_date=end_date,
            contact_email=contact_email,
            contact_phone=contact_phone,
        )

        booking.save()
        return Response({"message": "Booking successful"}, status=status.HTTP_201_CREATED)