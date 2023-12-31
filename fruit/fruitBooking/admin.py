from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(fruitItem)

@admin.register(fruitBooking)
class fruitBookingAdmin(admin.ModelAdmin):
    list_display = ('fruit_name', 'buyer', 'seller', 'fruit_requested', 'start_date', 'contact_email', 'contact_phone')

    