from django.db import models

# Create your models here.

class FoodItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://cdn-icons-png.freepik.com/256/11680/11680860.png")

    def __str__(self):
        return f"{self.item_name} - ${self.item_price}"