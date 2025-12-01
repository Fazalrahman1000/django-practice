from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItem

def index(request):
    food = FoodItem.objects.all()
    
    context = {
        'item':food
    }
    return render(request,'foods/index.html', context)

def item(request, item_id):
    id = item_id
    return render(request, id)

