from rest_framework import serializers
from .models import Pago, Recibo


class PagoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='servicio.cliente.nombre', read_only=True)
    
    class Meta:
        model = Pago
        fields = '__all__'
        read_only_fields = ['fecha_pago']


class ReciboSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='pago.servicio.cliente.nombre', read_only=True)
    monto = serializers.DecimalField(source='pago.monto', max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Recibo
        fields = '__all__'
        read_only_fields = ['fecha_emision']
