from django.shortcuts import render
from .models import User, UserAdmSite
from .serializers import userSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['GET','POST'])
def createListUser(request):

    user = UserAdmSite.objects.all()

    if request.method == 'GET':
       serializer = userSerializer(user, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
    
       
    
    if request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def updateDelete(request,pk):


    if request.method == 'GET':
        try:
            user = UserAdmSite.objects.get(pk=pk)
        except UserAdmSite.DoesNotExist:
            return Response ({"Erro" : "this user not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = userSerializer(user)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        try:
            user = UserAdmSite.objects.get(pk=pk)
        except UserAdmSite.DoesNotExist:
            return Response (status=status.HTTP_404_NOT_FOUND)
        
        serializer = userSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        
        if request.method == 'DELETE':
            try:
                user = UserAdmSite.objects.get(pk=pk)
            except UserAdmSite.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
            user.delete()
            return Response({f"User removed: {user}"}, status=status.HTTP_400_BAD_REQUEST)
        
                

