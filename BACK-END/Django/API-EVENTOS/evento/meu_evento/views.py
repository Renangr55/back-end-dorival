from django.shortcuts import render
from .models import Evento
from django.utils import timezone
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
        data = request.query_params.get('data_hora', None)
        quantidade = request.query_params.get('quantidade', None)        

        if categoria:
            eventos = Evento.objects.filter(categoria__icontains=categoria)
        
        if data:
            data_formatada = datetime.strptime(data, "%Y-%m-%d").date()
            eventos = Evento.objects.filter(data_hora__date=data_formatada)

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






@api_view(['GET','PUT','DELETE'])
def alterar_deletar_evento(request,pk):

    #listando um evento específico
    if request.method == 'GET':
        try:
            evento = Evento.objects.get(pk=pk)
        except Evento.DoesNotExist:
            return Response ({"ERRO" : "Evento não encontrado"}, status=status.HTTP_400_BAD_REQUEST)

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
    data = datetime.today().date()

    #comibinando a data com o dia e a hora
    data_completa = datetime.combine(data, datetime.min.time())
    
    #conventendo o datetime para um datetime aware,ela adiciona informações de fuso horário do django no datetime baseda na configuração TIME_ZONE nas settings
    data_aware = timezone.make_aware(datetime.combine(data, datetime.min.time()))
    

    diasParaEventos = data_aware + timedelta(days=7)

    #usando a propriedade range para retornar o intervalo da data de hoje a data daqui 7 dias
    filtrando_eventos = Evento.objects.all().filter(data_hora__range = [data, diasParaEventos])
    
    #retornan um serializer com a filtragem dos eventos
    eventos_serializer = EventoSerializer(filtrando_eventos, many=True)
    return Response(eventos_serializer.data, status=status.HTTP_200_OK)
    




