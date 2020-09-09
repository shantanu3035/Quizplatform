from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView



urlpatterns = [
    path('', dashboard, name='dashboard-dispatcher'),
    
    #path('admin/', admin.site.urls, name="dashboard-admin"),
]