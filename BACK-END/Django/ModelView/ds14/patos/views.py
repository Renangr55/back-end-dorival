from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Patinho
from .serializers import PatosSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers
# Create your views here.

class PatoPaginacao(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class PatoListCreateAPIView(ListCreateAPIView):
    queryset = Patinho.objects.all()
    serializer_class = PatosSerializer
    pagination_class = PatoPaginacao

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


