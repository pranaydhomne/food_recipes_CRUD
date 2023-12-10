from django.db import models

# Create your models here.
from django.db import models

class FoodRecipe(models.Model):
    food_name = models.CharField(max_length=255)
    food_description = models.TextField()
    food_image = models.ImageField(upload_to='food')

    def __str__(self):
        return self.food_name