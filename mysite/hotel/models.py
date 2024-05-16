from django.db import models
from django.utils import timezone

# Create your models here.

# tuple é uma lista que não pode ser mudada
tuple_quartos = (
    ('SOLTEIRO', 'solteiro'),
    ('CASAL', 'casal'),
    ('CONFORTO', 'conforto'),
    ('LUXO', 'luxo')
)
#O maior aparece no banco de dados e outro aparece para o usuário

class hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="logo/")
    
    def __str__(self):
        return self.titulo

class Quarto(models.Model):
    tipo = models.CharField(max_length=15, choices=tuple_quartos)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=255)
    foto_quarto = models.ImageField(upload_to="Foto_Quarto/")

    def __str__(self):
        return self.tipo
    
class user(models.Model):
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idade = models.IntegerField()
    endereco = models.CharField(max_length=50)
    quarto = models.CharField(max_length=15, choices=tuple_quartos)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
