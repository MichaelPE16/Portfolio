import pytest
from django.contrib.auth.models import User
from dealermfx.models import table_vehicles
import time
from dealermfx.views import update_Vehicle

@pytest.mark.slow
def test_sunm():
    time.sleep(2)
    assert 1 == 1

@pytest.mark.django_db # this decorator to asign a django_db property to the actual test
def test_user(): 
    User.objects.create_user('Test_user', 'MIchael@gmail.com', 'Maicol123')
    assert User.objects.count() == 1
    
    
@pytest.mark.django_db
def test_Vehicles_table(): 
    tables = table_vehicles.objects.all()
    print(list(tables))
    assert list(tables) == []


def Test_upodated(): 
    hello = update_Vehicle.return_value = 1
    assert hello ==  1