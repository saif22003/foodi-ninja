from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('customer_app.urls')),   # >>>> http://127.0.0.1:8000/customer/register/   <<<<
    path('resturant/', include('resturant_app.urls')), # >>>> http://127.0.0.1:8000/resturant/register/  <<<<
    path('food/', include('food_items_app.urls')),     # >>>> http://127.0.0.1:8000/food/items/ <<<<
]



