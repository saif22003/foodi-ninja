from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResturantSerializer

class Resturant_Regi_View(APIView):
    def post(self, request):
        serializer = ResturantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Resturant registered successfully in DATABASE."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
