from django.urls import path
from . import views


urlpatterns = [
    path('alunos/', views.listar_alunos),
    path('alunos/<int:pk>/', views.detalhe_aluno),
    path('alunos/criar/', views.criar_aluno),
    path('alunos/<int:pk>/', views.detalhe_aluno),
    path('alunos/alterar/<int:pk>/', views.alterar_aluno),
    path('alunos/apagar/<int:pk>/', views.deletar_aluno), # <int:pk>/ é uma chave primaria que para acessar determinada funcionalidade pelo end point precisa de um número inteiro
    

]