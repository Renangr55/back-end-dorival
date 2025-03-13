from django.urls import path
from . import views


urlpatterns = [
    path('alunos/', views.listar_alunos),
    path('alunos/criar/', views.criar_aluno),
    path('alunos/<int:pk>/', views.detalhe_aluno),
    path('alunos/alterar/<int:pk>/', views.alterar_aluno),
    path('alunos/apagar/<int:pk>/', views.deletar_aluno),
    path('faz_algo/<str:texto>' , views.macharete),

]