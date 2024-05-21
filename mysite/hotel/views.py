from django.shortcuts import render, HttpResponse, redirect
from .models import hotel, Quarto, user
from .forms import NameForm, FormCadastro, FormLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login 

# Create your views here.
def homepage(request):
    #dicionario para salvar os dados do banco
    context = {}
    #adicionamos os todos os objetos de hotel à variável.
    dados_hotel = hotel.objects.all()
    #adicionamos o objeto ao dicionario.
    context["dados_hotel"] = dados_hotel
    if request.user.is_authenticated:
        return render(request, 'homepage.html', context)
    else:
        return render(request, 'homepage2.html', context)

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
    

def cadastro(request):
    context = {}
    dados_quarto = Quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    dados_hotel = hotel.objects.all()
    context['dados_hotel'] = dados_hotel
    if request.method == "POST":
        form = FormCadastro (request.POST)
        if form.is_valid():
            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_password = form.cleaned_data['password']
       
            user = User.objects.create_user(username=var_user, email=var_email, password=var_password)
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()
            return redirect('/')
    else:
        form = FormCadastro()
        context['form'] = form
        return render(request, 'cadastro.html', context )
    
def login(request):
    context = {}
    dados_quarto = Quarto.objects.all()
    context['dados_quarto'] = dados_quarto
    dados_hotel = hotel.objects.all()
    context['dados_hotel'] = dados_hotel
    if request.method == "POST":
        form = FormLogin (request.POST)
        if form.is_valid():
            var_user = form.cleaned_data['user']
            var_password = form.cleaned_data['password']

            user = authenticate(username=var_user, password=var_password)
            if user is not None:
                return redirect('/')
            else:
                return HttpResponse("<h1>Usuário ou senha incorretos</h1>")
    else:
        form = FormLogin()
        context['form'] = form
        return render(request, 'login.html', context )

# def reserva(request):
#     if not request.user.is_authenticate:
#         return render(request, "login.html", {'form', form})
#     else:
#         return HttpResponse("<h1>RESERVA DE QUARTO</h1>")