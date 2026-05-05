from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Zolitron 2.")

def data(request):
    return HttpResponse({"abc": "test"})