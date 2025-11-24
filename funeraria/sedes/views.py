from rest_framework import viewsets
from .models import Sede
from .serializers import SedeSerializer


class SedeViewSet(viewsets.ModelViewSet):
    """CRUD para sedes"""
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    filterset_fields = ['activa', 'ciudad']
    search_fields = ['nombre', 'ciudad']
