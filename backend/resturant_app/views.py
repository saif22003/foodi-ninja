from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Resturant_Model

class Resturant_Regi_View(APIView):
    def post(self, request):
        resturant_data = request.data

        resturant_info = Resturant_Model.objects.create(
            resturant_name = resturant_data.get("resturant_name"),  
            resturant_phone = resturant_data.get("resturant_phone"),
            resturant_email = resturant_data.get("resturant_email"),  
            address = resturant_data.get("address"),  
            founded_on = resturant_data.get("founded_on"),  
        )
        print("Address:", resturant_data.get("address"))
        return Response(
            {"message": "Resturant registered successfully in DATABASE."},
            status=status.HTTP_201_CREATED
        )
 
 


