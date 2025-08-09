# resturant_app/serializers.py
from rest_framework import serializers
from .models import Resturant_Model

class ResturantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturant_Model
        fields = '__all__'

    def validate_phone(self, value):
        if Resturant_Model.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Phone number already exists.")
        return value

    def validate_email(self, value):
        if Resturant_Model.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
