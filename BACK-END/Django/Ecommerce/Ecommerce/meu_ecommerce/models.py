from django.db import models

# Create your models here.

class Produtos(models.Model):
    tituloProduto = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    image = models.ImageField(upload_to='ecommerce/', blank=True, null= True)
    data_criacao = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.tituloProduto
