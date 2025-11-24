from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import TipoServicio, Servicio
from .serializers import TipoServicioSerializer, ServicioSerializer


class TipoServicioViewSet(viewsets.ModelViewSet):
    """CRUD para tipos de servicios"""
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer
    filterset_fields = ['activo']


class ServicioViewSet(viewsets.ModelViewSet):
    """CRUD para servicios"""
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    filterset_fields = ['cliente', 'tipo_servicio', 'sede']
    search_fields = ['cliente__nombre', 'observaciones']


# Vistas de ejercicios básicos
@api_view(['POST'])
def costo_servicio(request):
    """Ejercicio 1: Calcula costo total (base + adicionales)"""
    try:
        costo_base = float(request.data.get('base') or request.data.get('costo_base', 0))
        adicionales = float(request.data.get('adicionales', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    costo_total = costo_base + adicionales
    return Response({
        "base": costo_base,
        "adicionales": adicionales,
        "total": costo_total
    })


@api_view(['GET'])
def calcular_gastos(request):
    """Ejercicio 2: Calcula gastos multiplicados por 1-10"""
    try:
        gasto = float(request.query_params.get('gasto', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametro 'gasto' inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    multiplicadores = [
        {"multiplicador": i, "resultado": gasto * i} 
        for i in range(1, 11)
    ]
    
    return Response({
        "gasto": gasto,
        "multiplicadores": multiplicadores,
    })
