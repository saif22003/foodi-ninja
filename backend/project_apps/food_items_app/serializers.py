from rest_framework import serializers
from project_apps.resturant_app.models import Resturant_Model
from .models import Food_Items_Model

class Food_Items_Model_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Items_Model
        fields = '__all__'

    def validate_resturant_phone(self, value):
        if not Resturant_Model.objects.filter(resturant_phone=value).exists():
            raise serializers.ValidationError("This restaurant is not registered in the database.")
        return value


    def validate_food_items(self, value):
        if Food_Items_Model.objects.filter(food_items_name=value).exists() :
            raise serializers.ValidationError("This item is already exists.")
        return value
    
    