from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Patinho (models.Model):
    nome = models.CharField(max_length=20)
    especie = models.CharField(max_length=150)
    idade = models.PositiveIntegerField()
    peso = models.FloatField()
    cor = models.CharField(max_length=50)
    superPoder = models.CharField(max_length=200)
    cagaTorrada = models.BooleanField(null=True, blank=True)

    def __str__(self):
        if self.cagaTorrada:
            return f'{self.nome} caga torradas perfeitas'
        return f'{self.nome} caga torradas perfeitas'
    
class DonoDoPato(AbstractUser):
    nome_dono = models.CharField(max_length=10, blank=True, null=True)
    photos = models.ImageField(upload_to='photos_perfil/', null=True, blank=True)
    bio = models.TextField(max_length=112)

    def __str__(self):
        return self.nome_dono