from rest_framework import serializers
from .models import Andamio, Alquiler, Cliente

class AlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alquiler
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class AndamioSerializer(serializers.ModelSerializer):
    andamio = serializers.CharField(read_only=True, source="andamio.id")
    andamio_id = serializers.PrimaryKeyRelatedField(queryset=Andamio.objects.all(), source="token")
    nombrelote = serializers.CharField(required=True, min_length=3)

    def validate_name(self, value):
        exist = Andamio.objects.filter(nombre__iexact=value).exists()

        if exist:
            raise serializers.ValidationError("Este andamio ya está registrado")

        return value

    class Meta:
        model = Andamio
        fields = '__all__'
