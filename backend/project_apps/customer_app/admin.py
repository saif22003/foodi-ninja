from django.contrib import admin
from .models import Customer_Model

@admin.register(Customer_Model)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name', 
        'customer_phone', 
        'status'
                    )

    ordering = ["id"]
