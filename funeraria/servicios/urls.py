from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tipos', views.TipoServicioViewSet, basename='tipo-servicio')
router.register(r'', views.ServicioViewSet, basename='servicio')

urlpatterns = [
    path('', include(router.urls)),
    path('basico/costo/', views.costo_servicio),
    path('basico/gastos/', views.calcular_gastos),
]
