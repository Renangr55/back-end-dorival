from rest_framework import serializers
from .models import Patinho , DonoDoPato
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patinho
        fields = '__all__'
        read_only_fields = ['id','cagaTorrada']

class DonoDoPatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonoDoPato
        fields = '__all__'

''''
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, atrss): # o atrss vai ser o atributo que pega as informações 
        username = atrss.get('username')
        password = atrss.get('password')
        if username and password:
            usuario = authenticate(request=self.context.get('request'),
                                   username=username, password=password)
            if not usuario:
                mensagem = "Crendenciais não identificada"
                raise serializers.ValidationError(mensagem, code='authorization')
            
            if not usuario.is_active:
                mensagem = "Conta nã identificada"
                raise serializers.ValidationError(mensagem, code='authorization')
            
            refresh = RefreshToken.for_user(usuario)
            atrss['usuario'] = usuario
            atrss['refresh'] = str(refresh)
            atrss['acess'] = str(refresh.access_token)

            return atrss
        else:
            mensagem = 'Usename ou senha não inseridos'
            raise serializers.ValidationError(mensagem, code='authorization')
'''

class LoginSerializer2(TokenObtainPairSerializer):
    def validate(self, attrs):
        dados = super().validate(attrs)
        dados['usuario'] = {
            'nome' : self.user.username,
            'bio' : self.user.bio
        }

        return dados