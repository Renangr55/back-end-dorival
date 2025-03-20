from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.listar_criar_evento),
    path('eventos/<int:pk>/' , views.alterar_deletar_evento),
    path('eventos/<int:pk>/' , views.alterar_deletar_evento ),
    path('eventos/proximos/' , views.eventosExibindo)
]