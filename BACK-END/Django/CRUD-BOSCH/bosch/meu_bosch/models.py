from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()
    descricao = models.TextField(max_length=200)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Livros"
    

    
