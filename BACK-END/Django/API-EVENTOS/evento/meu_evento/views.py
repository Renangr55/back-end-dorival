from django.shortcuts import render
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta


# Create your views here.

@api_view(['GET', 'POST'])
def listar_criar_evento(request,categoria=None,data=None, quantidade=None):   
    
    eventos = Evento.objects.all()

    #listando eventos
    if request.method == 'GET':
      

        categoria = request.query_params.get('categoria', None)
        data = request.query_params.get('data', None)
        quantidade = request.query_params.get('quantidade', None)        

        if categoria:
            eventos = Evento.objects.filter(categoria__icontains=categoria)
        
        if data:
            eventos = Evento.objects.filter(data_hora__icontains=data)

        if quantidade:
            try:
                eventos = eventos[0:int(quantidade)]  # Limita a quantidade de resultados
            except ValueError:
                return Response({"error": "Quantidade deve ser um número"}, status=status.HTTP_400_BAD_REQUEST)
            
        
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    
    
    



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

    #listando um evento específico
    if request.method == 'GET':
        try:
            evento = Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            return Response ({"ERRO" : "Aluno não encontrado"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EventoSerializer(evento)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
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
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def eventosExibindo(request):
    data = datetime.today().strftime('%Y-%m-%d')
    data_evento = datetime.strptime(data, '%Y-%m-%d')
    diasParaEventos = (data_evento + timedelta(days=7)).strftime('%Y-%m-%d')

    subindo_eventos = Evento.objects.all().filter(event_date__gt = data).filter(event_date__lte = diasParaEventos)
    subindoEventosSerializer = EventoSerializer(subindo_eventos, many=True)
    return Response(subindo_eventos.data, status=status.HTTP_200_OK)
    




