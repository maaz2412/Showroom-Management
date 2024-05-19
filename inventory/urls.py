from django.contrib import admin
from django.urls import path
from inventory import views
 
urlpatterns = [
    path('add_to_inventory/', views.add_to_inventory, name='inventory'),
    path('inventory_list/', views.display_inventory, name='inventory-list'),
    path('showroom/<int:showroom_id>/cars/', views.view_showroom, name='view_showroom'),
]