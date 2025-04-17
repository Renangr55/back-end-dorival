from django.urls import path
from .views import UsuarioListCreateApiView,UsuarioPaginacao,UsuarioRetrieveUpdateDestroyAPIView, LoginView

urlpatterns = [
    path('usuarios/',UsuarioListCreateApiView.as_view(), name='usuario-criar-listar' ),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyAPIView.as_view(), name='usuario-especifico'),
    path('logar/',LoginView.as_view(),name='logar' )
]