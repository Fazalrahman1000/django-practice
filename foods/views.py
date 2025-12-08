from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FoodItem
from .forms import FoodItemForm

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

def create_item(request):
    form = FoodItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foods:index')
    return render(request, 'foods/create_item.html', {'form': form})