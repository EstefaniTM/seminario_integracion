from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

@api_view(['POST'])
@permission_classes([AllowAny])
def area_triangulo(request):
    try:
        base = float(request.data.get('base', 0))
        altura = float(request.data.get('altura', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    area = (base * altura) / 2
    return Response({
        "base": base,
        "altura": altura,
        "area": area
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def tabla_multiplicar(request):
    try:
        n = int(request.query_params.get('numero', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    tabla = [f"{n}x{i}={n*i}" for i in range(1, 11)]
    return Response({
        "numero": n,
        "tabla": tabla,
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def contar_mayores(request):
    try:
        numeros = request.data.get('numeros', [])
        limite = float(request.data.get('limite', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        lista_numeros = [float(n) for n in numeros]
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    contador = 0
    for n in lista_numeros:
        if n > limite:
            contador += 1
    return Response({
        "numeros": lista_numeros,
        "limite": limite,
        "mayores": contador
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def sumar_por_frecuencia(request):
    try:
        numeros = request.data.get('numeros', [])
        limite = float(request.data.get('limite', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        lista_numeros = [float(n) for n in numeros]
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    frecuencia = {}
    for n in lista_numeros:
        if n >= limite:
            frecuencia[n] = frecuencia.get(n, 0) + 1
    
    resultado = 1
    i = 1
    while resultado + i <= limite:
        resultado += 1
        i+= 1
    return Response({
        "limite": limite,
        "resultado": resultado
    })



@api_view(['POST'])
@permission_classes([AllowAny])
def suma_total(request):
    try:
        numeros = request.data.get('numeros', [])
        limite = float(request.data.get('limite', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        lista_numeros = [float(n) for n in numeros]
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Sumar solo los números >= límite
    suma = 0
    for n in lista_numeros:
        suma+=n
    resultado = suma / len(lista_numeros)
    
    return Response({
        "numeros": lista_numeros,
        "promedio": resultado
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def potencia(request):
    try:
        base = float(request.data.get('base', 0))
        exponente = float(request.data.get('exponente', 0))
    except (TypeError, ValueError):
        return Response({"error": "Parametros invalidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    resultado = base ** exponente
    return Response({
        "base": base,
        "exponente": exponente,
        "resultado": resultado
    })