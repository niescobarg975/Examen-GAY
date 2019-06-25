from django.shortcuts import render, redirect
from .models import DuenoE, Arrendatario, Vehiculo
from Usuarios.models import User


# Create your views here.
def index(request):
    return render(request,'index.html')

def registro(request):
    return render(request,'registro.html')

def nav(request):
    return render(request,'navbar.html')

def administrador(request):
    dueno = DuenoE.objects.all()
    arren = Arrendatario.objects.all()
    vehiculo = Vehiculo.objects.all()
    usuarios = User.objects.all()
    contexto = {'dueno':dueno, 'arren':arren, 'vehiculo':vehiculo, 'usuarios':usuarios}
    return render(request, 'administrador.html', contexto)

def crearD(request):
    rut = request.POST.get('rut')
    email = request.POST.get('email')
    nombre = request.POST.get('nombre')
    telefono = request.POST.get('telefono')
    contrasenia = request.POST.get('contrasenia')
    direccion = request.POST.get('direccion')
    cuentaB = request.POST.get('cuenta')
    edificio = request.POST.get('edificio')
    piso = request.POST.get('piso')
    numero =  request.POST.get('numero')

    

    dueno = DuenoE(rut = rut, email = email, nombre = nombre, telefono = telefono, direccion = direccion, cuentaB= cuentaB,
                    edificio= edificio, piso = piso, numero = numero)

    us = User.objects.create_user(email = email, rut = rut, password = contrasenia, tipo = 'due')
    us.save()
    dueno.save()
    return render(request, 'index.html')


def crearA(request):
    rut = request.POST.get('rut')
    email = request.POST.get('email')
    nombre = request.POST.get('nombre')
    tarjeta = request.POST.get('tarjeta')
    banco = request.POST.get('banco')
    telefono = request.POST.get('telefono')
    contrasenia = request.POST.get('contrasenia')

    usu = Arrendatario(rut = rut, email = email, nombre = nombre,tarjeta = tarjeta,banco = banco 
    , telefono = telefono)

    us = User.objects.create_user(email = email, rut = rut, password = contrasenia, tipo = 'arr')
    us.save()
    usu.save()
    return render(request,'index.html')

def crearV (request):
    rutUsuario = request.POST.get('rutU')
    patente = request.POST.get('patente')
    marca = request.POST.get('marca')
    modelo = request.POST.get('modelo')
    anio = request.POST.get('anio')

    veh = Vehiculo(rutUsuario=rutUsuario, patente=patente, marca=marca, modelo = modelo, anio=anio)
    veh.save()
    return render(request, 'index.html')

