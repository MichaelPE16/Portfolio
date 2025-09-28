from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import SalesUser
from django import forms

# Custom form for Sales User registration
class SalesUserCreationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create your views here.

def home(request): 
    return render(request, 'homescreen.html')

@login_required(login_url='login')
def dashboard(request):
    # Check if user is a sales user
    try:
        sales_user = SalesUser.objects.get(user=request.user)
        if sales_user.is_sales_user:
            return render(request, 'dashboard.html')
    except SalesUser.DoesNotExist:
        # Redirect non-sales users
        return redirect('home')
    
    return redirect('home')

def signup(request): 
    if request.method == 'GET': 
        return render(request, 'signup.html', {'form': SalesUserCreationForm})
    else: 
        form = SalesUserCreationForm(request.POST)
        if form.is_valid(): 
            # Create the user
            user = form.save()
            
            # Create the associated SalesUser
            company_name = form.cleaned_data.get('company_name')
            sales_user = SalesUser(user=user, company_name=company_name)
            sales_user.save()
            
            # Log the user in
            login(request, user)
            return redirect('dashboard')
        else: 
            return render(request, 'signup.html', {'form': SalesUserCreationForm, 'error': 'Error creating user'})

def login_view(request): 
    if request.method == 'GET': 
        return render(request, 'login.html', {'form': AuthenticationForm})
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None: 
            return render(request, 'login.html', {'form': AuthenticationForm, 'error': 'User does not exist'})
        
        # Check if this is a sales user
        try:
            sales_user = SalesUser.objects.get(user=user)
            if sales_user.is_sales_user:
                login(request, user)
                return redirect('dashboard')
        except SalesUser.DoesNotExist:
            return render(request, 'login.html', {'form': AuthenticationForm, 'error': 'Not a sales user account'})
        
        return redirect('home')

