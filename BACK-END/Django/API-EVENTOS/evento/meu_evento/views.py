from django.shortcuts import render
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['GET', 'POST'])
def listar_criar_evento(request,categoria=None,data=None, quantidade=None):   
    
    #listando eventos
    if request.method == 'GET':
        evento = Evento.objects.all()
        serializer = EventoSerializer(evento, many=True)

        categoria = request.query_params.get('categoria', None)
        data = request.query_params.get('data', None)
        quantidade = request.query_params.get('quantidade', None)

        

        if categoria:
            eventos = Evento.objects.filter(evento_categoria_icontains=categoria)
        
        if data:
            eventos = Evento.objects.filter(evento_data_icontains=data)

        if quantidade:
            try:
                eventos = eventos[:int(quantidade)]  # Limita a quantidade de resultados
            except ValueError:
                return Response({"error": "Quantidade deve ser um número"}, status=status.HTTP_400_BAD_REQUEST)

    
    #Criando um evento
    if request.method == 'POST':
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data)



@api_view(['PUT','DELETE'])
def alterar_deletar_evento(request,pk):
    # alterando evento
    if request.method == 'PUT':
        try:
            evento = Evento.objects.get(pk=pk)

        except Evento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventoSerializer(evento, data=request.data)
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        
    #Excluindo evento
    if request.method == 'DELETE':
        try:
            evento = Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
        evento.delete()
        return Response({'EVENTO EXCLUIDO!!'}, status=status.HTTP_204_NO_CONTENT)
        #return Response(status=status.HTTP_400_BAD_REQUEST)

    #listando um evento específico
    if request.method == 'GET':
        try:
            evento = Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            return Response ({"ERRO" : "Aluno não encontrado"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = EventoSerializer(evento)
    return Response(serializer.data, status=status.HTTP_200_OK)



