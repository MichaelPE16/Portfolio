from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# now here is the user registrations model
class SalesUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    is_sales_user = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username
