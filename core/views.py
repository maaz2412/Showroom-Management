from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

# Create your views here.
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