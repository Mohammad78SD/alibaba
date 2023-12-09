from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Airport(models.Model):
    name = models.CharField(max_length= 255)
    No = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    address = models.TextField()
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
    
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE)
    name = models.CharField(max_length= 255)
    no = models.CharField(max_length= 10)
    capacity = models.IntegerField()
    price = models.FloatField()
    