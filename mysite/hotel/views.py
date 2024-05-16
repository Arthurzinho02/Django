from django.shortcuts import render, HttpResponse
from .models import hotel, Quarto, user
from .forms import NameForm

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

def nomeForm(request):
    context = {}
    dados_quarto = Quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    dados_hotel = hotel.objects.all()
    context['dados_hotel'] = dados_hotel
    
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_sobrenome = form.cleaned_data['sobrenome']
            var_email = form.cleaned_data['email']
            var_idade = form.cleaned_data['idade']
            var_endereco = form.cleaned_data['endereco']
            var_quarto = form.cleaned_data['quarto']
            var_data = form.cleaned_data['data']
            usuario = user(nome=var_nome, sobrenome=var_sobrenome ,email=var_email, idade=var_idade, endereco=var_endereco, quarto=var_quarto, data=var_data)
            usuario.save()
            return HttpResponse("<h1>thanks</h1>")
    else:
        form = NameForm()
        context['form'] = form
        return render(request, 'reservar.html', context )