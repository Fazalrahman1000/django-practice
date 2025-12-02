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
    item = FoodItem.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, 'foods/item.html', context)

