from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('project_apps.customer_app.urls')),   # >>>> http://127.0.0.1:8000/customer/register/   <<<<
    path('resturant/', include('project_apps.resturant_app.urls')), # >>>> http://127.0.0.1:8000/resturant/register/  <<<<
    path('food/', include('project_apps.food_items_app.urls')),     # >>>> http://127.0.0.1:8000/food/items/ <<<<
]



