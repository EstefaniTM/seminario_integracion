from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import TipoServicio, Sede, Cliente, Servicio, Pago
from ..serializers import (
    TipoServicioSerializer, SedeSerializer, ClienteSerializer,
    ServicioSerializer, PagoSerializer
)


# ViewSets para CRUD automático
class TipoServicioViewSet(viewsets.ModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer


class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


# Vistas de los 6 ejercicios básicos
@api_view(['POST'])
def costo_servicio(request):
    """Ejercicio 1: Calcula costo total (base + adicionales)"""
    try:
        costo_base = float(request.data.get('costo_base', 0))
        adicionales = float(request.data.get('adicionales', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    costo_total = costo_base + adicionales
    return Response({
        "costo_base": costo_base,
        "adicionales": adicionales,
        "costo_total": costo_total
    })


@api_view(['GET'])
def calcular_gastos(request):
    """Ejercicio 2: Calcula gastos multiplicados por cantidad"""
    try:
        gastos_unitarios = int(request.query_params.get('gastos', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    detalles = [f"Gasto {i}: ${gastos_unitarios * i}" for i in range(1, 11)]
    return Response({
        "gastos_unitarios": gastos_unitarios,
        "detalles": detalles,
    })


@api_view(['POST'])
def clientes_premium(request):
    """Ejercicio 3: Cuenta clientes con pago > límite"""
    try:
        montos = request.data.get('montos', [])
        monto_minimo = float(request.data.get('monto_minimo', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        lista_montos = [float(m) for m in montos]
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    contador = 0
    for m in lista_montos:
        if m > monto_minimo:
            contador += 1
    return Response({
        "montos": lista_montos,
        "monto_minimo": monto_minimo,
        "clientes_premium": contador
    })


@api_view(['POST'])
def ingresos_por_tipo(request):
    """Ejercicio 4: Suma ingresos por frecuencia (tipo de servicio)"""
    try:
        ingresos = request.data.get('ingresos', [])
        monto_minimo = float(request.data.get('monto_minimo', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        lista_ingresos = [float(n) for n in ingresos]
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    frecuencia = {}
    for ingreso in lista_ingresos:
        if ingreso >= monto_minimo:
            frecuencia[ingreso] = frecuencia.get(ingreso, 0) + 1
    
    total = 0
    detalle = {}
    for ingreso, freq in frecuencia.items():
        suma_ingreso = ingreso * freq
        total += suma_ingreso
        detalle[ingreso] = {"frecuencia": freq, "suma": suma_ingreso}
    
    return Response({
        "ingresos": lista_ingresos,
        "monto_minimo": monto_minimo,
        "detalle": detalle,
        "total": total
    })


@api_view(['POST'])
def ingresos_total(request):
    """Ejercicio 5: Suma total de ingresos >= límite"""
    try:
        ingresos = request.data.get('ingresos', [])
        monto_minimo = float(request.data.get('monto_minimo', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        lista_ingresos = [float(n) for n in ingresos]
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    suma = 0
    ingresos_sumados = []
    for ingreso in lista_ingresos:
        if ingreso >= monto_minimo:
            suma += ingreso
            ingresos_sumados.append(ingreso)
    
    return Response({
        "ingresos": lista_ingresos,
        "monto_minimo": monto_minimo,
        "ingresos_sumados": ingresos_sumados,
        "total": suma
    })


@api_view(['POST'])
def comisiones(request):
    """Ejercicio 6: Calcula comisiones (base^exponente)"""
    try:
        monto_base = float(request.data.get('monto_base', 0))
        porcentaje = float(request.data.get('porcentaje', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    comision = monto_base ** (porcentaje / 100)
    return Response({
        "monto_base": monto_base,
        "porcentaje": porcentaje,
        "comision": comision
    })
