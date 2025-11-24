from django.db import models
from servicios.models import Servicio


class Pago(models.Model):
    """Pagos realizados por servicios"""
    METODOS = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de Crédito'),
        ('transferencia', 'Transferencia'),
        ('cheque', 'Cheque'),
    ]
    
    servicio = models.OneToOneField(Servicio, on_delete=models.CASCADE, related_name='pago')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo = models.CharField(max_length=50, choices=METODOS)
    referencia = models.CharField(max_length=100, blank=True)
    pagado = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-fecha_pago']
    
    def __str__(self):
        return f"Pago ${self.monto} - {self.servicio.cliente.nombre}"


class Recibo(models.Model):
    """Recibos/Facturas de servicios"""
    numero = models.CharField(max_length=50, unique=True)
    pago = models.OneToOneField(Pago, on_delete=models.CASCADE, related_name='recibo')
    fecha_emision = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    observaciones = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-fecha_emision']
    
    def __str__(self):
        return f"Recibo {self.numero}"
