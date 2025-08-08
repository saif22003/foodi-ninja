from django.urls import path
from .views import Customer_Regi_View

urlpatterns = [
    path (
    # CUSTOMER REGISTRATION LINK =>>>>>>>> http://127.0.0.1:8000/customer/register/
  route = 'register/',
  view = Customer_Regi_View.as_view(),
  name = 'customer_register'
    ), 
]
