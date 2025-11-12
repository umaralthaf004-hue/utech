# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('kontak/submit/', views.submit_kontak, name='submit_kontak'), 
]