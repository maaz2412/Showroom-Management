from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('home/', views.home_view , name='home'),
    path('services/', views.services, name='services'),
    path('accounts/', views.accounts_view, name='accounts'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('manage/', views.manage_showroom, name='manage'),
    path('about/',views.about, name='about'),
    path('delete/',views.delete_showroom, name='delete')
]
