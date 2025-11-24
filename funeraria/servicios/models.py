from django.db import models
from usuarios.models import Cliente
from sedes.models import Sede


class TipoServicio(models.Model):
    """Tipos de servicios: Cremación, Entierro, Velatorio, etc."""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_dias = models.IntegerField(default=1)
    activo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    """Instancia de un servicio contratado"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='servicios')
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    fecha_contratacion = models.DateTimeField(auto_now_add=True)
    fecha_servicio = models.DateField()
    costo_base = models.DecimalField(max_digits=10, decimal_places=2)
    adicionales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-fecha_contratacion']
    
    def __str__(self):
        return f"Servicio {self.id} - {self.cliente.nombre}"
    
    def save(self, *args, **kwargs):
        """Calcula automáticamente el costo total"""
        self.costo_total = self.costo_base + self.adicionales
        super().save(*args, **kwargs)
