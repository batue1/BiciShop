from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Tienda.models import Producto, Tipos_Bicicleta, Rodado, Color, Material_Cuadro, Estado_Pedido
from Tienda.Carrito import Carrito

# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    return render (request, 'tienda.html', {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    # En la BD la clave de Producto es producto
    bicicleta = Producto.objects.get(producto=producto_id)
    #producto = Producto.objects.get(id=producto_id)
    #carrito.agregar(producto)
    carrito.agregar(bicicleta)
    return redirect("Tienda")

def eliminar_producto (request, producto_id):
    carrito = Carrito(request)
    #producto = Producto.objects.get(id=producto_id)
    producto = Producto.objects.get(producto=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto (request, producto_id):
    carrito = Carrito(request)
    #producto = Producto.objects.get(id=producto_id)
    producto = Producto.objects.get(producto=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito (request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")



#Poner el siguiente decorador arriba de las funciones vista que no se pueda acceder
#a menos que se esté logueado
#@login_required(login_url='home')