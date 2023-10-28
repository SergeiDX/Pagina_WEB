from django.contrib import admin
from .models import Pedido , LineaPedido, Envio, Banco, Estado, Tarjeta, Paqueteria
# Register your models here.

admin.site.register([Pedido, LineaPedido, Envio, Banco, Estado, Tarjeta, Paqueteria])