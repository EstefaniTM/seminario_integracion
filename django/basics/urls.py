from django.urls import path
from . import views

urlpatterns = [
    path('basic/area-triangulo', views.area_triangulo),
    path('basic/tabla-multiplicar', views.tabla_multiplicar),
    path('basic/contar-mayores', views.contar_mayores),
    path('basic/sumar-por-frecuencia', views.sumar_por_frecuencia),
    path('basic/suma-total', views.suma_total),
    path('basic/potencia', views.potencia)
]