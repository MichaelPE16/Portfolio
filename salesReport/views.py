from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def home(request): 
    return render(request, 'home.html')

def dashboard(request): 
    return render(request, '')