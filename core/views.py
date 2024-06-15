from typing import Any
from django.shortcuts import render, redirect
from core.models import Showroom
from inventory.models import Car
from customers.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def search(request):
    if request.method == 'GET':
        search_type = request.GET.get('search_item')
        if search_type == 'showrooms':
            user = request.user
            showrooms = Showroom.objects.filter(user=user)
            return render(request, 'core/search_showroom.html', {'showrooms':showrooms})
        elif search_type == 'inventory':
            user = request.user
            cars = Car.objects.filter(user=user).select_related('showroom')
            return render(request,'core/search_inventory.html', {'cars':cars})

        elif search_type == 'customers':
            user = request.user
            customers = Customer.objects.filter(user=user).prefetch_related('cars')
            return render(request,'core/search_customers.html', {'customers':customers})
        else:
            return JsonResponse('Invalid Option Selected')
    else:
        return redirect('home')



#Home page view

def about(request):
    return render(request, 'core/about.html')
def manage_showroom(request):
    user = request.user
    showrooms = Showroom.objects.filter(user=user)
    return render(request, 'core/manage_showroom.html', {'showrooms':showrooms})
def home_view(request):
    return render(request, 'core/home.html')
def accounts_view(request):
    return render(request, 'core/account.html')
#Main page view
#Services page view
def services(request):
    user=request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        capacity = request.POST.get('capacity')
        new_showroom = Showroom(name=name, location=location, capacity=capacity, user=user)
        new_showroom.save()
        if new_showroom:
            request.session['user_showroom_count'] = Showroom.objects.filter(user=user).count()
            return redirect('inventory')
        else:
            pass
    return render(request, 'core/services.html')
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_user = User(username=username, email=email, password=password)
        new_user.set_password(password)
        new_user.save()
        if new_user:
                login(request, new_user)
                return redirect('home')
        else:
            return redirect('register')
    else:
        return render(request, 'core/register.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        valid_user = authenticate(request, username=username, password=password)
        print(valid_user)
        if valid_user is not None:
            login(request, valid_user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Credentials")
    else:
        return render(request, 'core/login.html')
def logout_view(request):
    logout(request)
    messages.success(request, 'Your logged out, Login again to visit site')
    return redirect('login')
def delete_showroom(request):
    if request.method == 'POST':
        showroom_id = request.POST.get('showroom_id')
        showroom_to_delete = Showroom.objects.filter(pk=showroom_id)
        showroom_to_delete.delete()
        return JsonResponse({'message': 'Showroom deleted successfully.'})
    else:
         return JsonResponse({'Error showroom Not deleted'})
def showroom_list(request):
    showrooms = Showroom.objects.filter(user=request.user)
    return render(request, 'core/showroom_list.html', {'showrooms':showrooms})
def edit_showroom(request, showroom_id):
    if request.method=='POST':
        showroom = Showroom.objects.get(user=request.user, pk=showroom_id)
        showroom.name = request.POST.get('name')
        showroom.location = request.POST.get('location')
        showroom.capacity = request.POST.get('capacity')
        showroom.save
        return redirect('showroom_list')
    else:
        return render(request, 'core/services.html')
class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user

        showrooms = Showroom.objects.filter(user=current_user)
        cars = Car.objects.filter(user=current_user).select_related('showroom')
        customers = Customer.objects.filter(user=current_user).prefetch_related('cars')

        context['Showrooms_registered'] = showrooms.count()
        context['Cars_registered'] = cars.count()
        context['Customers_registered'] = customers.count()

        return context
    def get(self, request, *args, **kwargs):
        # Additional GET request handling logic if needed
        return super().get(request, *args, **kwargs)