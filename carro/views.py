from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.
def Carrito_compra(request):
    return render(request,'carrito.html')

def agregar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto=Producto.objects.get(id=producto_id)
    
    carro.agregar(producto=producto)
        
    return redirect('carrito_compra')

def eliminar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto=Producto.objects.get(id=producto_id)
        
    carro.eliminar(producto=producto)
    
    return redirect('carrito_compra')

def restar_producto(request, producto_id):
    
    carro=Carro(request)
    
    producto=Producto.objects.get(id=producto_id)
    
    carro.restar_producto(producto=producto)
    
    return redirect('carrito_compra')

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect('carrito_compra')