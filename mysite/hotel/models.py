from django.db import models

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
    valor = models.FloatField(max_length=9999)
    descricao = models.TextField(max_length=255)
    foto_quarto = models.ImageField(upload_to="Foto_Quarto/")

    def __str__(self):
        return self.tipo
