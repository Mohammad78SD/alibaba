from django.urls import path
from .views import list,list2

urlpatterns = [
    path('list', list, name="list" )
] 
urlpatterns = [
    path('airport_list', list2, name="airport_list" )
] 