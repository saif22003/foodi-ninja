from django.db import models
from _applib.model_utils import PhoneValidator


class Food_Items_Model(models.Model):

    resturant_phone = models.CharField(max_length=11, validators=[PhoneValidator()], unique=True)
    food_items_name = models.CharField(max_length=30)
    description = models.TextField(max_length= 256)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
 
    def __str__(self):
        return self.food_items_name

    
    class Meta:
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"
        db_table = "food_items"



