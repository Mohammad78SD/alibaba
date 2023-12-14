from django.contrib import admin
from .models import Flight, Airport

# Register your models here.

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    autocomplete_fields = ['origin']

@admin.register(Airport)
class FlightAdmin(admin.ModelAdmin):
    list_display = ["name","No","city","phone_number"]
    search_fields = ["name",]
    list_filter = ['name','city']