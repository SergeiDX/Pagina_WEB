from django.shortcuts import render

# Create your views here.
def Carrito_Compra(request):
    return render(request, 'carrito.html')