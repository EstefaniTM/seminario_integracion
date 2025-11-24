from django.contrib import admin
from .models import Sede


@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'telefono', 'gerente', 'activa']
    list_filter = ['activa', 'ciudad']
    search_fields = ['nombre', 'ciudad']
