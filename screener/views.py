from django.shortcuts import render

# Create your views here.

def screener(request): 
    return render(request, 'screener.html')