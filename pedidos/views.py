from django.shortcuts import render, redirect
from carro.carro import Carro
from pedidos.models import LineaPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.
def pedido2(request):
    return render(request, 'pedido.html')

def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))
        
        
        
    LineaPedido.objects.bulk_create(lineas_pedido)
    return redirect('tienda')

    #enviar_mail(
    #    pedido=pedido,
     #   lineas_pedido=lineas_pedido,
      #  nombreusuario=request.user.username,
       # emailusuario=request.user.usermail
    #)
    
    
def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido2.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario")
    })
    
    mensaje_texto = strip_tags(mensaje)
    
    from_email="whitelite695@gmail.com"
    #to= kwargs.get("emailusuario")
    to = kwargs.get("albert_af2000@hotmail.com")
    send_mail(asunto, mensaje_texto,from_email, [to],html_message=mensaje)