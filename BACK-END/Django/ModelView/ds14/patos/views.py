from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Patinho
from .serializers import PatosSerializer,  DonoDoPatoSerializer, LoginSerializer2
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class PatoPaginacao(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class PatoListCreateAPIView(ListCreateAPIView):
    queryset = Patinho.objects.all()
    serializer_class = PatosSerializer
    pagination_class = PatoPaginacao
    permission_classes = [IsAuthenticated] #serve para escolher quem está com permição

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('none')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    def perform_create(self, serializer):
        if serializer.validated_data['peso'] < 0:
            raise serializers.ValidationError("o peso não pode ser negativo")
        serializer.save()


class PatoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Patinho.objects.all()
    serializer_class = PatosSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        idade = request.data.get('idade')
        if int(idade) < 20:

            #tem 2 jeitos de fazer

            data = request.data.copy()
            data['cor'] = 'Verde'
            request._full_data=data
            
        return super().put(request, *args, **kwargs)

'''
class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create (self, request, *args, **Kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.validated_data['usuario']
        usuario_serializer = DonoDoPatoSerializer(usuario)

        return Response({
            'usuario': usuario_serializer.data,
            'refresh': serializer.validated_data['refresh'],
            'acess': serializer.validated_data['acess']

        },status=status.HTTP_200_OK)
    
'''

class loginView2(TokenObtainPairView):
    serializer_class = LoginSerializer2


