from django.contrib import admin
from .models import *

admin.site.register(Field)
# admin.site.register(Booking)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('fieldOwner','owner_name', 'farmer', 'acres_requested', 'start_date', 'end_date', 'contact_email', 'contact_phone')
