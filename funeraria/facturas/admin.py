from django.contrib import admin
from .models import Pago, Recibo


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['id', 'monto', 'metodo', 'fecha_pago', 'pagado']
    list_filter = ['metodo', 'pagado', 'fecha_pago']


@admin.register(Recibo)
class ReciboAdmin(admin.ModelAdmin):
    list_display = ['numero', 'fecha_emision']
    search_fields = ['numero']
