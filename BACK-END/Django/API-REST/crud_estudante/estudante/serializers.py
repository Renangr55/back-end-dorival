from rest_framework import serializers
from .models import Aluno

class AlunoSerializer(serializers.ModelSerializer): #gerando todos os campos da classe Aluno
    class Meta:
        model = Aluno    
        fields = '__all__' 






