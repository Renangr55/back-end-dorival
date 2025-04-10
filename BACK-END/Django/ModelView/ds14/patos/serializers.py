from rest_framework import serializers
from .models import Patinho 
class PatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patinho
        fields = '__all__'
        read_only_fields = ['id','cagaTorrada']