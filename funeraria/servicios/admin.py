from django.contrib import admin
from .models import TipoServicio, Servicio


@admin.register(TipoServicio)
class TipoServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio_base', 'duracion_dias', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre']


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'tipo_servicio', 'costo_total', 'fecha_servicio']
    list_filter = ['tipo_servicio', 'sede', 'fecha_contratacion']
    search_fields = ['cliente__nombre']
