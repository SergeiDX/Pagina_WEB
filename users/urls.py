from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('registro/',views.VRegistro.as_view(), name='registro'),
    path('cerrar_sesion/',views.cerrar_sesion, name='cerrar_sesion'),
    path('logear/',views.logear, name='logear'),
]
