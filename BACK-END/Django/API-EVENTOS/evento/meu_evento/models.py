from django.db import models

# Create your models here.
class Evento (models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    local = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_hora = models.DateTimeField()
    categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.nome