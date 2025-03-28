from django.db import models

# Create your models here.

class User (models.Model):
    name = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    telephone = models.CharField(max_length=15)  
    address = models.CharField(max_length=200)  
    education = models.CharField(max_length=10)
    numbersAnimals = models.CharField(max_length=10)

    def __str__(self):
        return self.nome