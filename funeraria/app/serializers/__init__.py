from rest_framework import serializers
from ..models import TipoServicio, Sede, Cliente, Servicio, Pago


class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServicio
        fields = '__all__'


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ServicioSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    tipo_servicio_nombre = serializers.CharField(source='tipo_servicio.nombre', read_only=True)
    
    class Meta:
        model = Servicio
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    servicio_cliente = serializers.CharField(source='servicio.cliente.nombre', read_only=True)
    
    class Meta:
        model = Pago
        fields = '__all__'
