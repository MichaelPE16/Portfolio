from django.urls import URLPattern, path

from Portfolio import urls
from . import views

urlpatterns =[
path('', views.home, name = 'home'),
path('dashboard/', views.dashboard, name = "dashboard"),
path('signup/', views.signup, name = "signup"),
path('login/', views.login_view, name = "login"),
]