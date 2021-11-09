from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

## Formulario para creación de usuario
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# Create your views here.   
#-------------------------------------------------------------------------------------#
def register(request):
    #Chequeadmos si ya esta autenticado
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()

    if  request.method == 'POST': #Si ya mandó el formulario
        form = CreateUserForm(request.POST) #Crear el usuario
        if form.is_valid(): #Si el formulario es válido
            form.save() #Guarda el usuario DJANGO se encarga de encriptar la pass
            #Para que le indique al usuario que su cuenta fue creada
            usuario = form.cleaned_data.get('username')
            messages.success(request, 'Usuario %s fue creado' % (usuario))
            return redirect('login') #Llamamos al método

    context = {'form': form}
    return render(request, 'register.html', context)

#------------------------------------------------------------------------------------#
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    #Chequeamos si ya se logeó
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Autenticamos que el usuario exista en la BD
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Usuario o contraseña incorrecto' )
    context ={}

    return render(request, 'login.html', context)
#-------------------------------------------------------------------------------------#
def logoutUser(request):
    logout(request)
    return redirect('login')

#-------------------------------------------------------------------------------------#
def home(request):
    context = {}
    return render(request, 'home.html', context)

#-------------------------------------------------------------------------------------#
#Poner el siguiente decorador arriba de las funciones vista que no se pueda acceder
#a menos que se esté logueado
#@login_required(login_url='home')