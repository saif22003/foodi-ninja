from django.urls import path
from .views import Food_Items_Model_View

urlpatterns = [
    path (
    # RESTURANT REGISTRATION LINK =>>>>>>>> http://127.0.0.1:8000/food/items/
  route = 'items/',
  view = Food_Items_Model_View.as_view(),
  name = 'food-items'
    ), 
]
