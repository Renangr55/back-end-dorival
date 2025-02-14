from django.shortcuts import render
from .models import Produto

# Create your views here.

def lista_atividade(request):
    produtos = Produto.objects.all().order_by('-data_criacao')
    return render(request, 'Ecommerce_Renan/lista_produtos.html',{'produtos': produtos})


