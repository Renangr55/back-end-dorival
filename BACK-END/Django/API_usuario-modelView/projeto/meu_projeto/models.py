from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario(AbstractUser):
    biografia = models.TextField(max_length=200, blank=False ,null=True)
    idade = models.PositiveIntegerField(null=True)
    telefone = models.PositiveIntegerField(null=True)
    endereco = models.TextField(max_length=200,blank=False,null=True)
    escolaridade = models.TextField(max_length=200,blank=False,null=True)
    animas = models.PositiveIntegerField(null=True)
   
    def __str__(self):
        return self.username
    
     
    