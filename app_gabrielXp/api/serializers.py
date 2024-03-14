from rest_framework import serializers
from .models import Dados

class DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = '__all__'  

class DadosCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = ['Botao', 'Sensor', 'ResetContador']  
