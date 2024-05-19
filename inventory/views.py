from django.shortcuts import render, redirect
from inventory.models import Car
from core.models import Showroom
# Create your views here.
def view_showroom(request, showroom_id):
       items = Car.objects.filter(showroom_id=showroom_id)
       return render(request, 'inventory/inventory_list.html', {'items':items})
def add_to_inventory(request):
        if request.method == 'POST':
                user = request.user
                car_name = request.POST.get('name')
                car_model = request.POST.get('model')
                showroom_id = request.POST.get('showroom')
                showroom = Showroom.objects.get(pk=showroom_id)
                car_brand = request.POST.get('brand')
                car_price = request.POST.get('price')
                new_car = Car(car_name=car_name, car_model=car_model, car_brand=car_brand, showroom=showroom, car_price=car_price)
                new_car.save()
                return redirect('inventory-list')
        elif request.method == 'GET':
               user = request.user
               user_showroom_count = request.session.get('user_showroom_count', 0)
               showrooms = Showroom.objects.filter(user=user)
               brands = Car.Brands.choices
               return render(request, 'inventory/add_to_inventory.html', {'user_showroom_count': user_showroom_count, 'showrooms':showrooms,'brands':brands })
        else:
            showrooms = Showroom.objects.filter(user=user)
            brands = Car.Brands.choices
            return render(request, 'inventory/add_to_inventory.html', {'brands':brands , 'showrooms':showrooms})
def display_inventory(request):
       items = Car.objects.all()
       return render(request, 'inventory/inventory_list.html', {'items': items})