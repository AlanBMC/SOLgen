from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criasessao/', views.cria_sessao_produtos, name='criasessao'),
    path('atualiza_produtos/', views.atualiza_produtos, name='atualiza_produtos'),
    path('automacao_de_cadastro/', views.envia_pro_pyautogui, name='automacao_de_cadastro'),
    path('atualiza_banco/', views.atualiza_banco_view, name='atualiza_banco'),
    
]
