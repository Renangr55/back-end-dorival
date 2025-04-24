from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveDestroyAPIView
from .models import Usuario
from .serializers import LoginSerializer, UsuariosSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status


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
    permission_classes = [IsAuthenticated]


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"Mensagem" : f" deletado com sucesso"}, status=status.HTTP_204_NO_CONTENT)
    

   
    

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
                
