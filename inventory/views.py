from django.shortcuts import render, redirect
from inventory.models import Car
from django.http import JsonResponse
from core.models import Showroom
# Create your views here.

def add_to_inventory(request):
        if request.method == 'POST':
                user = request.user
                car_name = request.POST.get('name')
                car_model = request.POST.get('model')
                showroom_id = request.POST.get('showroom')
                showroom = Showroom.objects.get(pk=showroom_id, user=user)
                car_brand = request.POST.get('brand')
                car_price = request.POST.get('price')
                user = request.user
                new_car = Car(car_name=car_name, user=user, car_model=car_model, car_brand=car_brand, showroom=showroom, car_price=car_price)
                new_car.save()
                showroom.capacity -= 1
                showroom.save()
                return redirect('car_list')
        elif request.method == 'GET':
               user = request.user
               user_showroom_count = request.session.get('user_showroom_count', 0)
               showrooms = Showroom.objects.filter(user=user)
               brands = Car.Brands.choices
               return render(request, 'inventory/add_to_inventory.html', {'user_showroom_count': user_showroom_count, 'showrooms':showrooms,'brands':brands })
def delete_car(request):
       if request.method == 'POST':
              car_id = request.POST.get('car_id')
              car_to_delete = Car.objects.get(pk=car_id)
              car_to_delete.delete()
              return JsonResponse({'success': True, 'message': 'Car deleted successfully'})
       else:
              return JsonResponse({'Error Not deleted Successfully'})
def edit_car(request, car_id):
       car = Car.objects.get(user=request.user, pk=car_id)
       user = request.user
       if request.method == 'POST': 
              car.car_name = request.POST.get('name')
              car.car_model = request.POST.get('model')
              showroom_id = request.POST.get('showroom')
              car.showroom = Showroom.objects.get(pk=showroom_id)
              car.car_brand = request.POST.get('brand')
              car.car_price = request.POST.get('price')
              car.user = user
              car.save()
              return redirect('car_list')
       else:
              showrooms = Showroom.objects.filter(user=user)
              brands = Car.Brands.choices
              user_showroom_count = request.session.get('user_showroom_count', 0)
              return render(request, 'inventory/add_to_inventory.html', {'showrooms':showrooms, 'user_showroom_count': user_showroom_count, 'brands':brands })
def car_list(request):
       cars = Car.objects.filter(user=request.user).select_related('showroom')
       return render(request, 'inventory/car_list.html', {'cars':cars})