from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'pagos', views.PagoViewSet, basename='pago')
router.register(r'recibos', views.ReciboViewSet, basename='recibo')

urlpatterns = [
    path('', include(router.urls)),
    path('basico/clientes-premium/', views.clientes_premium),
    path('basico/ingresos-por-tipo/', views.ingresos_por_tipo),
    path('basico/ingresos-total/', views.ingresos_total),
    path('basico/comisiones/', views.comisiones),
]
