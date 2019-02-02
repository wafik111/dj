from django.shortcuts import render,redirect
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello hossam")


# Create your views here.
