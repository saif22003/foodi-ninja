from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Food_Items_Model_Serializer

class Food_Items_Model_View(APIView):
    def post(self, request):
        serializer = Food_Items_Model_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Successfully added a new food item in DATABASE."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

