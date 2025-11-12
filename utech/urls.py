# utech/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Arahkan root URL (/) ke myapp/urls.py
    path('', include('myapp.urls')), 
]