from django.contrib import admin
from django.urls import path
from inventory import views
 
urlpatterns = [
    path('add_to_inventory/', views.add_to_inventory, name='inventory'),
    path('delete_car/',views.delete_car, name='delete_car'),
    path('edit_car/<int:car_id>/', views.edit_car, name='edit_car'),
    path('car_list', views.car_list,name='car_list')
]