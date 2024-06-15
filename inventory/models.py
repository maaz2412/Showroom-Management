from django.db import models
from core.models import Showroom
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=30)
    car_model = models.IntegerField()
    car_price = models.IntegerField()
    showroom = models.ForeignKey(Showroom, null=False, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null =True)
    
 
    class Brands(models.TextChoices):
        HONDA = 'Honda', 'Honda'
        SUZUKI = 'Suzuki', 'Suzuki'
        TOYOTA = 'Toyota', 'Toyota'
    car_brand = models.CharField(
        max_length=10,
        choices=Brands.choices,
        default=None,
        null=True
    ) 
    def __str__(self):
        return self.car_name
