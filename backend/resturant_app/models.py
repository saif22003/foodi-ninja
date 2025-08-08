from django.db import models
from _applib.model_utils import PhoneValidator


class Resturant_Model(models.Model):

    resturant_name = models.CharField(max_length=30)
    resturant_phone = models.CharField(max_length=11, validators=[PhoneValidator()], unique=True)
    resturant_email = models.EmailField(max_length=254, unique=True)
    address = models.TextField(max_length= 256)
    founded_on = models.DateField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.resturant_name

    
    class Meta:
        verbose_name = "Resturant"
        verbose_name_plural = "Resturants"
        db_table = "resturant"



