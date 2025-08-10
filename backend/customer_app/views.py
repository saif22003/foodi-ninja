from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
import json
import requests

class Customer_Regi_View(APIView):

    def send_otp(self):
        url = "http://127.0.0.1:8001/otp/send/"

        payload = json.dumps({
            "otp_for" : "sms",
            "identifier" : self.request.data.get("customer_phone"),
            "reason" : "forgot pass",
        })

        headers = {
            'Content-Type' : 'application/json'
        }

        requests.request("POST", url, headers = headers, data = payload)


    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            self.send_otp()
            return Response(
                {"message": "Customer registered successfully in DATABASE."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
