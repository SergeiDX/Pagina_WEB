from django.urls import path
from . import views



urlpatterns = [
    path('',views.Carrito_compra,name='carrito_compra'),   
]
