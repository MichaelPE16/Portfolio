from turtle import Turtle
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class table_vehicles(models.Model): 
    name = models.CharField(max_length=150)
    model = models.CharField(max_length = 150 )
    year = models.DateField()
    rent= models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    description = models.TextField(max_length = 500, null = True, blank = True )
    image = models.TextField(max_length = 500, null = True, blank = True)
    rented = models.DateField(blank =True, null = True)

    
    def __str__(self):
        return self.name
