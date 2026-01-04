from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import FoodItem
from .forms import FoodItemForm

def index(request):
    food = FoodItem.objects.all()
    
    context = {
        'item':food
    }
    return render(request,'foods/index.html', context)

class IndexClassView(ListView):
    model = FoodItem
    template_name = 'foods/index.html'
    context_object_name = 'item'

    

def item(request, item_id):
    item = FoodItem.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, 'foods/item.html', context)


class DetailsClassView(DetailView):
    model = FoodItem
    template_name  = 'foods/item.html'
    


def create_item(request):
    form = FoodItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('foods:index')
    return render(request, 'foods/create_item.html', {'form': form})

def update_item(request, item_id):
    item = FoodItem.objects.get(id=item_id)
    form = FoodItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('foods:index')
    
    return render(request, 'foods/create_item.html', {'item':item, 'form':form})

def delete_item(request, item_id):
    item = FoodItem.objects.get(id=item_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('foods:index')
    
    return render(request, 'foods/item_delete.html', {'item':item})