from customers.models import Customer
from inventory.models import Car
from django.utils import timezone

def run():
    customer = Customer.objects.create(customer_name = 'Umar', date_purchased = timezone.now())
    customer.car.add(Car.objects.first())
    print(customer)
