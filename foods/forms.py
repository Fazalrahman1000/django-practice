from django.forms import ModelForm
from .models import FoodItem

class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['item_name', 'description', 'item_price', 'item_image']
