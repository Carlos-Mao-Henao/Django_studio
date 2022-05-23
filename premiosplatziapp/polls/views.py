from django.shortcuts import render
# Create a Http reponse
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello word")
#We create de Http response in this funtion