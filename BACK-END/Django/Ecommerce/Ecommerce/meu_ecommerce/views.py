from django.shortcuts import render, get_list_or_404
from .models import Produtos

# Create your views here.
def Lista_produtos(request):
    produtos = Produtos.objects.all().order_by('-data_criacao')
    return render(request,'meu_ecommerce/index.html',{'produtos': produtos})

def info_produto(request, produto_id):
    info = get_list_or_404(Produtos, id=produto_id)
    return render(request, 'meu_ecommerce/info.html', {'info' : info})
