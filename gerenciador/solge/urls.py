from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
]
