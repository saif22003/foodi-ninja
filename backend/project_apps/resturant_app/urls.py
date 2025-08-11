from django.urls import path
from .views import Resturant_Regi_View

urlpatterns = [
    path (
    # RESTURANT REGISTRATION LINK =>>>>>>>> http://127.0.0.1:8000/resturant/register/
  route = 'register/',
  view = Resturant_Regi_View.as_view(),
  name = 'resturant_details'
    ), 
]
