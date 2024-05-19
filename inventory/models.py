from django.db import models
from core.models import Showroom

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=30)
    car_model = models.IntegerField()
    car_price = models.IntegerField()
    showroom = models.ForeignKey(Showroom, null=False, default=None, on_delete=models.CASCADE)
    

    class Brands(models.TextChoices):
        HONDA = 'Honda', 'Honda'
        SUZUKI = 'Suzuki', 'Suuzki'
        TOYOTA = 'Toyota', 'Toyota'
    car_brand = models.CharField(
        max_length=10,
        choices=Brands.choices,
        default=None,
        null=True
    ) 
    def __str__(self):
        return self.car_name
