from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import Airport


# Create your views here.
def list(request):
    flights = {
        'name': 'iran air',
        'No': '1200',
        'capacity': 120,
        'price': 650000 
        }
    return JsonResponse(flights)


def list2(request):
    airports = Airport.objects.all()
    Airports_list = []
    for item in airports:
        dict = {
            "name" : item.name,
            "city" : item.city,
            "address" : item.address
        }
        Airports_list.append(dict)
    return HttpResponse(Airports_list)