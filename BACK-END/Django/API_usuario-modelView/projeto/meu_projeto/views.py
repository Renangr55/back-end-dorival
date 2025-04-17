from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView
from .models import Usuario
from .serializers import LoginSerializer, UsuariosSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class UsuarioPaginacao(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class UsuarioListCreateApiView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer
    pagination_class = UsuarioPaginacao
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset =  super().get_queryset()
        idade = self.request.query_params.get('idade')
        if idade:
            queryset = queryset.filter(nome__icontains=idade)
        return queryset
    
class UsuarioRetrieveUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosSerializer
    lookup_field = 'pk'

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
                
