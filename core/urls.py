from django.contrib import admin
from django.urls import path
from core import views
from .views import DashboardView

urlpatterns = [
    path('home/', views.home_view , name='home'),
    path('services/', views.services, name='services'),
    path('accounts/', views.accounts_view, name='accounts'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('manage/', views.manage_showroom, name='manage'),
    path('about/',views.about, name='about'),
    path('delete/',views.delete_showroom, name='delete'),
    path('search/', views.search, name='search'),
    path('delete_showroom/',views.delete_showroom, name='delete_showroom'),
    path('showroom_list/',views.showroom_list, name='showroom_list'),
    path('edit_showroom<int:showroom_id>/', views.edit_showroom, name='edit_showroom'),
    path('Dashboard/', DashboardView.as_view(), name='dashboard')
]
