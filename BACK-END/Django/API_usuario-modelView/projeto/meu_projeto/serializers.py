from rest_framework import serializers
from .models import Usuario
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Usuario
        fields = '__all__'

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        dados = super().validate(attrs)
        dados['usuario'] = {
            'nome' : self.user.username,
            'senha' : self.user.password,
            
        }

        return dados