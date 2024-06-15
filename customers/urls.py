from django.contrib import admin
from django.urls import path
from customers import views

urlpatterns = [
    path('add_customer/',views.add_customer, name='add'),
    path('delete_customer/',views.delete_customer, name='delete_customer'),
    path('edit_customer/<int:customer_id>/',views.edit_customer, name='edit_customer'),
    path('customer_list/',views.customer_list, name='customer_list')
]