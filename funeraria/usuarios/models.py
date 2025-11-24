from django.db import models


class Cliente(models.Model):
    """Cliente/Familia que contrata servicios"""
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-fecha_registro']
    
    def __str__(self):
        return self.nombre
