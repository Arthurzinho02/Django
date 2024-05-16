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
    

