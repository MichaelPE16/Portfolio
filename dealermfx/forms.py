from django.forms import ModelForm, widgets
from .models import table_vehicles
from django import forms

class vehicleForm(ModelForm): 
    class Meta:
        model = table_vehicles
        fields = ['name', 'model', 'year', 'rent', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-transparent border-info text-bg-dark ', 'PlaceHolder': 'Name'}),
            'model': forms.TextInput(attrs={'class': 'form-control bg-transparent border-info text-bg-dark ', 'PlaceHolder': 'Model'}),
            'year': forms.TextInput(attrs={'class': 'form-control bg-transparent border-info text-bg-dark ', 'PlaceHolder': 'Year'}),
            'rent': forms.TextInput(attrs={'class': 'form-control bg-transparent border-info text-bg-dark ', 'PlaceHolder': 'Rent'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-transparent border-info text-bg-dark ','rows': '3',  'PlaceHolder': 'Description'}),
            'image': forms.Textarea(attrs={'class': 'form-control bg-transparent border-info text-bg-dark ','rows': '3',  'PlaceHolder': 'image'})
        }
