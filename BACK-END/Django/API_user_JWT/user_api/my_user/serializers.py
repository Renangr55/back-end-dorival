from rest_framework import serializers
from .models import UserAdmSite

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdmSite
        fields = ['username', 'password', 'address', 'telephone']

    # criando uma função create que herda de serializer que cria e valida os dados e acaba armazenando
    def create (self, validated_data):
        user = UserAdmSite.objects.create_user(**validated_data)
        user.is_active = True  # Ativar o usuário automaticamente
        user.save()
        return user