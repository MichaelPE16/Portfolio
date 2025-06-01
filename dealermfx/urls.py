from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_vehicles, name = 'show_vehicles'),
    path('rented/', views.show_rented_Vehicles, name = 'rented_vehicles'),
    path('details/<int:id_vehicle>', views.vehicles_details, name = 'details'),
    path('update/<int:id_vehicle>', views.update_form, name = 'update'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout_page, name='logout'),
    path('create', views.create, name='create'),
    path('delete/<int:id_vehicle>', views.delete_vehicle, name='delete'),
    path('rented/<int:id_vehicle>', views.rented_vehicle, name= 'rented'),
] 