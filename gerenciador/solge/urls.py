from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro_produto', views.cadastro_produto, name='cadastro_produto'),
    path('ativapyautogui/', views.cadastra_produto_pyautogui, name='cadastra_produto_pyautogui')
]
