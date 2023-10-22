from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout, authenticate
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.

class VRegistro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request,'signup2.html',{"form":form})
    
    def post(self, request):
        form=UserCreationForm(request.POST)
        
        if form.is_valid():
            
            usuario=form.save()
        
            auth_login(request, usuario) 
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request,'signup2.html',{"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')
    
    
def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                auth_login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request,"Usuario no valido")
    form=AuthenticationForm()
    return render(request, 'login.html',{"form":form})

        



def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['contrasena'] == request.POST['confirmar-contrasena']:
            try:                
                user = User.objects.create_user(username=request.POST['nombre-usuario'],password=request.POST['contrasena'])
                
                user.save()
                login(request, user)
                return redirect('home')  
              
            except:
                return render(request,'signup.html',{"error2":'el usuario ya existe'})
        return render(request,'signup.html',{"error":'Las contraseñas no coinciden'})
        


def login(request):
    return render(request, 'login.html')
