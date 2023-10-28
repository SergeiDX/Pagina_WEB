from django.urls import path
from . import views
app_name = 'pedidos'
urlpatterns = [
    path('pedido2', views.pedido2, name='pedido2'),
    path('procesar', views.procesar_pedido, name="procesar_pedido"),
    path('envio', views.create, name='envio'),
]
