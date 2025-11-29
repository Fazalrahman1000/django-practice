from django.db import models

# Create your models here.

class FoodItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    item_price = models.IntegerField()

    def __str__(self):
        return f"{self.item_name} - ${self.item_price}"