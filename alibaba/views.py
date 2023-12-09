from django.http.response import HttpResponse, JsonResponse

def welcome(request):
    return HttpResponse('Welcome to Alibaba!')

def about(request):
    return HttpResponse('About Alibaba!')
def contact(request):
    return HttpResponse('Contact Alibaba!')

