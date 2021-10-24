from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.

#---------------------------------------------------------------------------------------------------------------#
class Tipos_Bicicleta(models.Model):
    tipo        = models.AutoField(primary_key= True) 
    descripcion = models.CharField(max_length= 100, null= False)
    
    def __str__(self):
          return self.descripcion

#---------------------------------------------------------------------------------------------------------------#
class Rodado(models.Model):
    rodado      = models.AutoField(primary_key= True) 
    descripcion = models.PositiveIntegerField(null= False,  validators=[MaxValueValidator(36), MinValueValidator(1)])

    def __str__(self):
          return '%s' % (self.descripcion)

#---------------------------------------------------------------------------------------------------------------#
class Color(models.Model):
    Tipo        = models.AutoField(primary_key= True) 
    descripcion = models.CharField(max_length= 60, null= False)

    def __str__(self):
          return self.descripcion

#---------------------------------------------------------------------------------------------------------------#
class Material_Cuadro(models.Model):
    color       = models.AutoField(primary_key= True) 
    descripcion = models.CharField(max_length= 100, null= False)

    def __str__(self):
          return self.descripcion

#---------------------------------------------------------------------------------------------------------------#
class Producto(models.Model):
    producto    = models.AutoField(primary_key= True)
    tipo        = models.ForeignKey(Tipos_Bicicleta, on_delete=models.SET_NULL, blank= False, null= True)
    rodado      = models.ForeignKey(Rodado, on_delete=models.SET_NULL, blank= False, null= True)
    color       = models.ForeignKey(Color, on_delete=models.SET_NULL, blank= False, null= True)
    material    = models.ForeignKey(Material_Cuadro, on_delete=models.SET_NULL, blank= False, null= True)
    descripcion = models.TextField(max_length=250, blank=True, validators=[MaxLengthValidator(250)])
    precio      = models.DecimalField(max_digits=10, decimal_places=2, default=150000.0)
    descuento   = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    cantidad    = models.IntegerField(null= False, default= 0)
    imagen      = models.ImageField('Foto', upload_to= "fotos" )
    publicar    = models.BooleanField()
    def __str__(self):
          return '%s, rodado %s '  % (self.tipo, self.rodado)

#---------------------------------------------------------------------------------------------------------------#
class Estado_Pedido(models.Model):
    estadoPedido = models.AutoField(primary_key= True) 
    descripcion  = models.CharField(max_length= 100, null= False)

    def __str__(self):
          return self.descripcion
#---------------------------------------------------------------------------------------------------------------#
class Forma_Pago(models.Model):
    formaPago   = models.AutoField(primary_key= True) 
    descripcion = models.CharField(max_length= 100, null= False)

    def __str__(self):
          return self.descripcion
#---------------------------------------------------------------------------------------------------------------#
class Pedidos_Cabecera(models.Model):
    pedido       = models.AutoField(primary_key= True) 
    cliente      = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    fechahora    = models.DateTimeField(auto_now=True, auto_now_add=False)
    formaPago    = models.ForeignKey(Forma_Pago, on_delete=models.SET_NULL, blank= False, null= True)
    estadoPedido = models.ForeignKey(Estado_Pedido, on_delete=models.SET_NULL, blank= False, null= True)

    def __str__(self):
          return 'N° %s'  % (self.pedido)
#---------------------------------------------------------------------------------------------------------------#

class Pedidos_linea(models.Model):
    pedido       = models.ForeignKey(Pedidos_Cabecera, on_delete=models.SET_NULL, blank=False, null=True)
    producto     = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=False, null=True)
    cantidad     = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    precioPedido = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
          return '%s - %s - %s $%s'  % (self.pedido, self.cantidad, self.producto, self.precioPedido)