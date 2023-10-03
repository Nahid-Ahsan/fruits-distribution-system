from django.db import models
from django.contrib.auth.models import User

class Field(models.Model):
    name = models.CharField(max_length=100)
    size_in_acres = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Booking(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    acres_requested = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
