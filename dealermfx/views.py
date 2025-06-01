from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from .models import table_vehicles
from .forms import vehicleForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from datetime import datetime


# Create your views here.

# show all vehicles availables
def show_vehicles(request):
    if request.method == 'POST': 
        search = request.POST["search"]
        vehicles  = table_vehicles.objects.filter(name__contains = search ,user = request.user, rent = False)
        return render(request, 'show_vehicles.html', {'vehicles': vehicles, 'rented':'Vehicles Not Rented', 'search':search})
    else: 
        vehicles  = table_vehicles.objects.filter(user = request.user, rent = False)
    return render(request, 'show_vehicles.html', {'vehicles': vehicles, 'rented':'Vehicles Not Rented'})

#show only rented vehicles
def show_rented_Vehicles(request):
    if request.method == 'POST': 
        search = request.POST["search"]
        vehicles  = table_vehicles.objects.filter(name__contains = search , user = request.user, rent = True)
        return render(request, 'show_vehicles.html', {'vehicles': vehicles, 'rented':'Vehicles Rented', 'search':search})
    else: 
        vehicles  = table_vehicles.objects.filter(user = request.user, rent = True)
    return render(request, 'show_vehicles.html', {'vehicles': vehicles, 'rented':'Vehicles Rented'})

#Use to show all vehicles details
def vehicles_details(request, id_vehicle):
    vehicle = get_object_or_404(table_vehicles, pk= id_vehicle, user = request.user)
    return render(request, 'details.html' , {'vehicle': vehicle})


#Details Vehicles funtions
def update_form(request, id_vehicle):

        if request.method == 'GET': 
            vehicle = get_object_or_404(table_vehicles,pk = id_vehicle, user = request.user)
            form = vehicleForm(instance = vehicle)
            return render(request, 'update_vehicle.html', {'vehicle': vehicle, 'form': form})
        else:
            try: 
                vehicle = get_object_or_404(table_vehicles, pk = id_vehicle, user = request.user)
                form = vehicleForm(request.POST, instance = vehicle)
                form.save()
                return redirect('show_vehicles')
            except ValueError: 
                return render(request, 'update_vehicle.html', {'vehicle': vehicle, 'form': form, 'error': 'NO data suported'})

#delete vehicle
def delete_vehicle(request, id_vehicle):
    vehicle = get_object_or_404(table_vehicles, pk = id_vehicle, user = request.user)
    if request.method == 'POST': 
        vehicle.delete()
        return redirect('show_vehicles')
    return redirect('show_vehicles')

#rented 
def rented_vehicle(request, id_vehicle): 
    vehicle = get_object_or_404(table_vehicles, pk =id_vehicle, user = request.user)
    if request.method == 'POST': 
        if vehicle.rent == False and (vehicle.rented == None or vehicle.rented < datetime.now()):
            vehicle.rented = datetime.now()
            vehicle.rent = True
            vehicle.save()
            return redirect('rented_vehicles')
        else: 
            vehicle.rented = False
            vehicle.save()
        return redirect('show_vehicles')




#sign up    
def signup(request): 
    
    if request.method == 'GET': 
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:  
            if request.POST['password1'] == request.POST['password2']: 
                try:
                    user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('show_vehicles')
                except IntegrityError:
                   return render(request, 'signup.html', {'form':UserCreationForm, 'error': 'User Already exists'})

    return render(request, 'signup.html', {'form':UserCreationForm, 'error': 'Password does not match'})



#sign in
def signin(request):
    if request.method == 'GET': 
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else: 
        user = authenticate(request, username =request.POST['username'],password =request.POST['password1'] )
        if user is None: 
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error': 'User does not exists'})
        login(request, user)
        return redirect('show_vehicles')
    

#logout
def logout_page(request): 
    logout(request)
    return redirect('signin')

#create_vehicle
def create(request): 
    if request.method == 'GET': 
       return render(request, 'create_vehicle.html', {'form': vehicleForm})
    else: 
        try:
            form = vehicleForm(request.POST)
            new_vehicle = form.save(commit=False)
            new_vehicle.user = request.user
            new_vehicle.save()
            return redirect('show_vehicles')
        except ValueError: 
            return (request, 'create_vehicle.html', {'form': vehicleForm, 'error': 'Error Adding Vehicle'})

