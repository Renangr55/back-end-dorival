from django.db import models

# Create your models here.

class Atividade(models.Model):
    titulo = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    descricao = models.TextField(max_length=200)
    data_atividade = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    