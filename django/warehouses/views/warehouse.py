from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Warehouse
from ..serializers import WarehouseSerializer

@api_view(["GET"])
def warehouse_get_list(request):
    """List all warehouses with optional search filtering"""
    qs = Warehouse.objects.all()
    q = (request.query_params.get("q") or "").strip()
    if q:
        qs = qs.filter(Q(code__icontains=q) |
                       Q(name__icontains=q) |
                       Q(city__icontains=q))
    data = WarehouseSerializer(qs, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def warehouse(request):
    """GET: list all warehouses; POST: create new warehouse"""
    if request.method == "GET":
        qs = Warehouse.objects.all()
        data = WarehouseSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = WarehouseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def warehouse_detail(request, warehouse_id: int):
    """GET: retrieve; PUT/PATCH: update; DELETE: delete warehouse"""
    try:
        warehouse = Warehouse.objects.get(pk=warehouse_id)
    except Warehouse.DoesNotExist:
        return Response(
            {'detail': 'Not found'},
            status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        return Response(WarehouseSerializer(warehouse).data, status=status.HTTP_200_OK)
    
    elif request.method in ["PUT", "PATCH"]:
        serializer = WarehouseSerializer(warehouse, data=request.data, partial=(request.method == "PATCH"))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "DELETE":
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["PUT"])
def waterhouse_get_by_id(request,waterhouse_id: int):
    try:
        warehouse = Warehouse.objects.get(pk=waterhouse_id)
    except warehouse.DoesNotExist:
        return Response(
            {
                'Detail': 'NotFoud'
            },
            status=status.HTTP_404_NOT_FOUND)
    serializer = WarehouseSerializer(isinstance=warehouse, data=request.data)
    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def warehouses_delete(request, warehouse_id: int):
    try:
        warehouse = Warehouse.objects.get(pk=warehouse_id)
    except Warehouse.DoesNotExist:
        return Response({'Detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    warehouse.delete()
    return Response({'Detail': 'Registro eliminado'}, status=status.HTTP_200_OK)
