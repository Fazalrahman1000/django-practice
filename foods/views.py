from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the foods index.</h1>")

def item(request):
    return HttpResponse("<h1>This is a food item page.</h1>")

