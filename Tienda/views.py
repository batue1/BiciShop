from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


#Poner el siguiente decorador arriba de las funciones vista que no se pueda acceder
#a menos que se esté logueado
#@login_required(login_url='home')