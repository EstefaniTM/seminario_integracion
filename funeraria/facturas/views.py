from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Pago, Recibo
from .serializers import PagoSerializer, ReciboSerializer


class PagoViewSet(viewsets.ModelViewSet):
    """CRUD para pagos"""
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    filterset_fields = ['metodo', 'pagado']


class ReciboViewSet(viewsets.ModelViewSet):
    """CRUD para recibos"""
    queryset = Recibo.objects.all()
    serializer_class = ReciboSerializer
    search_fields = ['numero', 'pago__servicio__cliente__nombre']


# Vistas de ejercicios básicos
@api_view(['POST'])
def clientes_premium(request):
    """Ejercicio 3: Cuenta montos > límite"""
    try:
        montos = request.data.get('montos', [])
        limite = float(request.data.get('limite', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        lista_montos = [float(m) for m in montos]
    except (TypeError, ValueError):
        return Response({"error": "Montos inválidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    montos_mayores = [m for m in lista_montos if m > limite]
    
    return Response({
        "montos": lista_montos,
        "limite": limite,
        "montos_mayores": montos_mayores,
        "cantidad": len(montos_mayores)
    })


@api_view(['POST'])
def ingresos_por_tipo(request):
    """Ejercicio 4: Suma ingresos por tipo de servicio con frecuencia >= límite"""
    try:
        servicios = request.data.get('servicios', [])
        montos = request.data.get('montos', [])
        limite = float(request.data.get('limite', 1))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    if len(servicios) != len(montos):
        return Response({"error": "servicios y montos deben tener igual longitud"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        lista_montos = [float(m) for m in montos]
    except (TypeError, ValueError):
        return Response({"error": "Montos inválidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Agrupar por tipo de servicio
    ingresos_por_tipo = {}
    frecuencia_tipo = {}
    
    for tipo, monto in zip(servicios, lista_montos):
        if tipo not in ingresos_por_tipo:
            ingresos_por_tipo[tipo] = 0
            frecuencia_tipo[tipo] = 0
        ingresos_por_tipo[tipo] += monto
        frecuencia_tipo[tipo] += 1
    
    # Filtrar por frecuencia >= límite
    tipos_filtrados = {
        tipo: ingresos_por_tipo[tipo]
        for tipo in ingresos_por_tipo
        if frecuencia_tipo[tipo] >= limite
    }
    
    return Response({
        "servicios": servicios,
        "montos": lista_montos,
        "limite": limite,
        "ingresos_por_tipo": ingresos_por_tipo,
        "tipos_con_frecuencia_mayor_igual": list(tipos_filtrados.keys())
    })


@api_view(['POST'])
def ingresos_total(request):
    """Ejercicio 5: Suma total de montos >= límite"""
    try:
        montos = request.data.get('montos', [])
        limite = float(request.data.get('limite', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        lista_montos = [float(m) for m in montos]
    except (TypeError, ValueError):
        return Response({"error": "Montos inválidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    montos_filtrados = [m for m in lista_montos if m >= limite]
    total = sum(montos_filtrados)
    promedio = total / len(montos_filtrados) if montos_filtrados else 0
    
    return Response({
        "montos": lista_montos,
        "limite": limite,
        "total": total,
        "promedio": promedio,
        "cantidad": len(montos_filtrados)
    })


@api_view(['POST'])
def comisiones(request):
    """Ejercicio 6: Calcula comisiones (base^exponente)"""
    try:
        base = float(request.data.get('base', 0))
        exponente = float(request.data.get('exponente', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        resultado = base ** exponente
    except (ValueError, ZeroDivisionError):
        return Response({"error": "Cálculo inválido"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({
        "base": base,
        "exponente": exponente,
        "resultado": resultado
    })
