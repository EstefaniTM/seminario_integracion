from django.urls import path
from . import views

urlpatterns = [
    path('warehouses/list', views.warehouse_get_list),
    path('warehouses', views.warehouse),
    path('warehouses/<int:warehouse_id>', views.warehouse_detail),
    path('warehouses/<int:warehouse_id>', views.warehouses_delete)
]