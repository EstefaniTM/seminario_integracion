from django.db import models


class TipoServicio(models.Model):
    """Tipos de servicios funerarios: Cremación, Entierro, etc."""
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre


class Sede(models.Model):
    """Sedes/Locaciones de la funeraria"""
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"


class Cliente(models.Model):
    """Clientes/Familias que contratan servicios"""
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    """Instancia de un servicio contratado"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    fecha_contratacion = models.DateTimeField(auto_now_add=True)
    fecha_servicio = models.DateField()
    costo_base = models.DecimalField(max_digits=10, decimal_places=2)
    adicionales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Servicio {self.id} - {self.cliente.nombre}"


class Pago(models.Model):
    """Pagos realizados por servicios"""
    servicio = models.OneToOneField(Servicio, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo = models.CharField(max_length=50, choices=[
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    ])
    
    def __str__(self):
        return f"Pago ${self.monto} - {self.servicio.cliente.nombre}"

