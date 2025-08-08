from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer_Model

class Customer_Regi_View(APIView):
    def post(self, request):
        customer_data = request.data

        customer_info = Customer_Model.objects.create(
            customer_name = customer_data.get("customer_name"),  
            customer_phone = customer_data.get("customer_phone"),
            customer_email = customer_data.get("customer_email"),  
            gender = customer_data.get("gender"),
            date_of_birth = customer_data.get("dob"),
            address =  customer_data.get("address"),
            password = customer_data.get("password"),  
        )

        return Response(
            {"message": "Customer registered successfully in DATABASE."},
            status=status.HTTP_201_CREATED
        )
 
 


