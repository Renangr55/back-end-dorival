from django.shortcuts import render
from .models import Atividade

# Create your views here.

def lista_atividade(request):
    atividades = Atividade.objects.all().order_by('-data_atividade')
    return render(request, 'to_do_list/lista_atividades.html', {'atividades': atividades})




