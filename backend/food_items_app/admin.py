from django.contrib import admin
from .models import Food_Items_Model

@admin.register(Food_Items_Model)
class Food_Items_Model_Admin(admin.ModelAdmin):
    list_display = (
        'resturant_phone', 
        'food_items_name',
        'is_available',
        )

    ordering = ["id"]
