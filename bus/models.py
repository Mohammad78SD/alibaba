from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Terminal(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(
            max_length=15,
            validators=[
                RegexValidator(
                    regex=r"^\+\d{1,3}\d{3}\d{3}\d{4}$",
                    message="Phone number must be in the format +XXX-XXX-XXXX.",
                )
            ],
        )
    open_time = models.TimeField()
    close_time = models.TimeField()
    
class BusTravel(models.Model):
    origin = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name="originating_travels")
    destination = models.ForeignKey(Terminal, on_delete=models.CASCADE, related_name="destination_travels")
    model = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    capacity = models.IntegerField()
    price = models.FloatField()
    operator = models.CharField(max_length=255)