from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criasessao/', views.cria_sessao_produtos, name='criasessao'),
    path('atualiza_produtos/', views.atualiza_produtos, name='atualiza_produtos'),
    
]
