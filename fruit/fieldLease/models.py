from django.db import models
from django.contrib.auth.models import User

class Field(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    size_in_acres = models.DecimalField(max_digits=5, decimal_places=2)
    lease_rate = models.DecimalField(max_digits=10, decimal_places=2)
    land_usage = models.TextField()

class Booking(models.Model):
    fieldOwner = models.ForeignKey(Field, on_delete=models.CASCADE)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=255) 
    acres_requested = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)