from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField
# Create your models here.
User = get_user_model()

class Paqueteria(models.Model):
    nombrepaq = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombrepaq
    
    
class Estado(models.Model):
    nombreEST = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombreEST

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            
            total = Sum(F("precio")*F("cantidad"), output_field = FloatField())
            
            
        )["total"]
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']
        
class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'Linea pedido'
        verbose_name_plural = 'Lineas Pedidos'
        ordering = ['id']
        
        
class Envio(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=40)
    Codigo_Postal = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    paqueteria = models.ForeignKey(Paqueteria, on_delete=models.CASCADE)

        
    class Meta:
        db_table = 'Envio'
        verbose_name= 'Envio'
        verbose_name= 'Envios'
        ordering = ['id']
        
        
    
    
        
class Banco(models.Model):
    nombrebanc= models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombrebanc

class Tarjeta(models.Model):
    numero_tarjeta = models.CharField(max_length=50)
    fecha_exp = models.CharField(max_length=50)
    cvv = models.CharField(max_length=50)
    nombrebanco = models.ForeignKey(Banco, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)