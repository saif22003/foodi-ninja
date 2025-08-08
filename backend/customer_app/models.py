from django.db import models
from _applib.model_utils import PhoneValidator, DOBValidator, GenderChoice


class Customer_Model(models.Model):

    customer_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=11, validators=[PhoneValidator()], unique=True)
    customer_email = models.EmailField(max_length=254, unique=True)
    gender = models.CharField(max_length=10, choices=GenderChoice.choices, default= GenderChoice.MALE)
    date_of_birth = models.DateField(null=True, blank=True, validators=[DOBValidator()])
    address = models.TextField()
    status = models.BooleanField(default=True)
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name

    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        db_table = "customer"


