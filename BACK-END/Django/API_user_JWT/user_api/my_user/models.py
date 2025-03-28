from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserAdmSite(AbstractUser):
    idade = models.PositiveIntegerField(null=True, blank=True)
    telephone = models.CharField(max_length=15)  
    address = models.CharField(max_length=200)  
    education = models.CharField(max_length=10)
    numbersAnimals = models.CharField(max_length=10)

    def __str__(self):
        return self.username



class User (models.Model):
    name = models.CharField(max_length=100)
    idadeUser = models.PositiveIntegerField(null=True, blank=True)
    enderecoUser = models.CharField(max_length=200)

    def __str__(self):
        return self.name