from django.db import models
from inventory.models import Car
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    quantity_cars = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, null =True)
    cars = models.ManyToManyField(Car)
    date_purchased = models.DateField()

@receiver(pre_delete, sender=Customer)
def delete_related_cars(sender, instance, **kwargs):
    # Delete all cars related to the customer being deleted
    instance.cars.clear()
