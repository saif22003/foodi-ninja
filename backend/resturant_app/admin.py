from django.contrib import admin
from .models import Resturant_Model

@admin.register(Resturant_Model)
class ResturantAdmin(admin.ModelAdmin):
    list_display = (
        'resturant_name', 
        'resturant_phone', 
        'status'
                    )

    ordering = ["id"]
