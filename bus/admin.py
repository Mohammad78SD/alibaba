from django.contrib import admin
from .models import Terminal, BusTravel


# Register your models here.
@admin.register(Terminal)
class FlightAdmin(admin.ModelAdmin):
    pass


@admin.register(BusTravel)
class FlightAdmin(admin.ModelAdmin):
    pass