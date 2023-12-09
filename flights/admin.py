from django.contrib import admin
from .models import Flight, Airport

# Register your models here.

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    pass

@admin.register(Airport)
class FlightAdmin(admin.ModelAdmin):
    pass