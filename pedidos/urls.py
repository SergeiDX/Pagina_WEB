from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedido2, name='pedido2'),
    path('', views.procesar_pedido, name="procesar_pedido"),
]
