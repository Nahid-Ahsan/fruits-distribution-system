from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Field, Booking
from .serializers import FieldSerializer
from .forms import BookingForm
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def field_list(request):
    # Get a list of available fields for lease
    fields = Field.objects.all()
    serializer = FieldSerializer(fields, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def field_detail(request, field_id):
    # Display details of a specific field
    try:
        field = Field.objects.get(id=field_id)
        serializer = FieldSerializer(field)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Field.DoesNotExist:
        return Response({'error': 'Field not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def book_field(request, field_id):
    # Handle booking a field
    field = Field.objects.get(id=field_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.field = field
            booking.farmer = request.user
            booking.save()
            return Response({'message': 'Field booked successfully!'}, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
