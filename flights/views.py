from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


# Create your views here.
def list(request):
    flights = {
        'name': 'iran air',
        'No': '1200',
        'capacity': 120,
        'price': 650000 
        }
    return JsonResponse(flights)