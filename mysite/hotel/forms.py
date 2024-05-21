from django import forms

tuple_quartos = (
    ('SOLTEIRO', 'solteiro'),
    ('CASAL', 'casal'),
    ('CONFORTO', 'conforto'),
    ('LUXO', 'luxo')
)
class NameForm(forms.Form):
    nome = forms.CharField(label="Nome:", max_length=100)
    sobrenome =  forms.CharField(label="Sobrenome:", max_length=50)
    email = forms.EmailField(label="Email:", max_length=150)
    idade = forms.IntegerField(label="Idade:", min_value=0)
    endereco = forms.CharField(label="Endereço:", max_length=50)
    quarto = forms.ChoiceField(label="Quarto:", choices=tuple_quartos)
    data = forms.DateTimeField(label="Data:", widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    
class FormCadastro(forms.Form):
    first_name = forms.CharField(label='Nome:', max_length=20)
    last_name = forms.CharField(label='Sobrenome:', max_length=20)
    user = forms.CharField(label='Usuário:', max_length=20)
    email = forms.EmailField(label='Email:', max_length=100)
    password = forms.CharField(label='Senha:', widget=forms.PasswordInput)

class FormLogin(forms.Form):
    user = forms.CharField(label='Usuário:', max_length=20)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)


