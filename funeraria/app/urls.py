from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tipos-servicio', views.TipoServicioViewSet, basename='tipo-servicio')
router.register(r'sedes', views.SedeViewSet, basename='sede')
router.register(r'clientes', views.ClienteViewSet, basename='cliente')
router.register(r'servicios', views.ServicioViewSet, basename='servicio')
router.register(r'pagos', views.PagoViewSet, basename='pago')

urlpatterns = [
    path('', include(router.urls)),
    # Ejercicios básicos
    path('funeraria/costo-servicio', views.costo_servicio),
    path('funeraria/calcular-gastos', views.calcular_gastos),
    path('funeraria/clientes-premium', views.clientes_premium),
    path('funeraria/ingresos-por-tipo', views.ingresos_por_tipo),
    path('funeraria/ingresos-total', views.ingresos_total),
    path('funeraria/comisiones', views.comisiones),
]

