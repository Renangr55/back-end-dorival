from django.db import models

# Create your models here.

class Produto(models.Model):
    tituloProduto = models.CharField(max_length=200)
    preco = models.FloatField()
    descricaoProduto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tituloProduto

    
    
