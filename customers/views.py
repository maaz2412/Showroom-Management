from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from customers.models import Customer
from django.utils import timezone
from inventory.models import Car
from django.shortcuts import get_object_or_404
# Create your views here.

def add_customer(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        quantity_cars = request.POST.get('capacity')
        date_purchased = timezone.now()
        user = request.user
        customer = Customer.objects.create(user=user,customer_name=customer_name, quantity_cars=quantity_cars,date_purchased=date_purchased )
        car_ids= request.POST.getlist('car_purchased')
        cars = Car.objects.filter(pk__in=car_ids)
        customer.cars.add(*cars)
        print(customer)
        return redirect('add')
    else:
        cars = Car.objects.all()
        return render(request, 'customers/add_customer.html', {'cars':cars})
def delete_customer(request):
    if request.method == 'POST':
        id_customer = request.POST.get('customer_id')
        customer_to_delete = Customer.objects.get(pk=id_customer)
        customer_to_delete.delete()
        return JsonResponse({'success': True, 'message': 'Customer with ID {} deleted successfully'})
    else:
        return JsonResponse({'failure': True, 'message': 'Unable to delete Customer'})
def edit_customer(request,customer_id):
    customer_to_edit = Customer.objects.get(pk=customer_id)
    print(customer_to_edit.id)
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        quantity_cars = request.POST.get('capacity')
        date_purchased = timezone.now()
        customer_to_edit.customer_name = customer_name
        customer_to_edit.quantity_cars = quantity_cars
        customer_to_edit.date_purchased = date_purchased
        customer_to_edit.save()
        print(customer_to_edit.id)
        return redirect('customer_list')
    else:
        cars = Car.objects.all()
        return render(request, 'customers/add_customer.html', {'cars':cars})

def customer_list(request):
    user = request.user
    customers = Customer.objects.filter(user=user).prefetch_related('cars')
    return render(request,'customers/customer_list.html', {'customers':customers})