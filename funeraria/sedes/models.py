from django.db import models


class Sede(models.Model):
    """Sedes/Sucursales de la funeraria"""
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    horario_atencion = models.CharField(max_length=100, default='24/7')
    gerente = models.CharField(max_length=100, blank=True)
    activa = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['ciudad', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"
