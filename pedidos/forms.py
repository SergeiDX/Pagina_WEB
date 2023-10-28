from django import forms
from .models import Estado, Paqueteria
from django.forms import ModelForm
from .models import Envio

class EnvioForm(ModelForm):
    class Meta:
        model = Envio
        fields = ['Nombre', 'Apellidos', 'Direccion', 'Telefono', 
                'Codigo_Postal', 'estado', 'paqueteria']