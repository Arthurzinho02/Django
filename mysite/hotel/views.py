from django.shortcuts import render, HttpResponse
from .models import hotel
from .models import Quarto

# Create your views here.
def homepage(request):
    #dicionario para salvar os dados do banco
    context = {}
    #adicionamos os todos os objetos de hotel à variável.
    dados_hotel = hotel.objects.all()
    #adicionamos o objeto ao dicionario.
    context["dados_hotel"] = dados_hotel
    return render(request, 'homepage.html', context)

def quartos(request):
    context = {}
    dados_quarto = Quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    dados_hotel = hotel.objects.all()
    context['dados_hotel'] = dados_hotel
    return render(request, 'quartos.html', context)