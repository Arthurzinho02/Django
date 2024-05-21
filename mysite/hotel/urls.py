from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('quarto', views.quartos, name="quarto"),
    path('reservar', views.nomeForm, name="reservar"),
    path('cadastro', views.cadastro, name="cadastro"),
    path('login', views.login, name="login")
]