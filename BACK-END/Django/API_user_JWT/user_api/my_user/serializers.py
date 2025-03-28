from rest_framework import serializers
from .models import User, UserAdmSite

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'adress', 'telephone']

    # criando uma função create que herda de serializer que cria e valida os dados e acaba armazenando
    def create (self, validated_data):
        user = UserAdmSite.objects.create_user(**validated_data)
        return user