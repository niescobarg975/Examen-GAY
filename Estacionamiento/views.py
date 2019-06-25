from django.shortcuts import render, redirect
from .models import duenoE, usuario, vehiculo


# Create your views here.
def index(request):
    return render(request,'index.html')

def registro(request):
    return render(request,'registro.html')

def perfil(request):
    return render(request,'perfil.html')

def disponibilidad(request):
    return render(request,'disponibilidad.html')    

def crearD(request):
    rut = request.POST.get('rut')
    email = request.POST.get('email')
    nombre = request.POST.get('nombre')
    telefono = request.POST.get('telefono')
    contrasenia = request.POST.get('contrasenia')
    direccion = request.POST.get('direccion')
    cuentaB = request.POST.get('cuenta')
    edificio = request.POST.get('edificio')

    dueno = duenoE(rut = rut, email = email, nombre = nombre, telefono = telefono, contrasenia = contrasenia,
    direccion = direccion, cuentaB= cuentaB, edificio= edificio)
    dueno.save()
    return redirect('index.html')


def crearU(request):
    rut = request.POST.get('rut')
    email = request.POST.get('email')
    nombre = request.POST.get('nombre')
    tarjeta = request.POST.get('tarjeta')
    banco = request.POST.get('banco')
    telefono = request.POST.get('telefono')
    contrasenia = request.POST.get('contrasenia')

    usu = usuario(rut = rut, email = email, nombre = nombre,tarjeta = tarjeta,banco = banco 
    , telefono = telefono, contrasenia = contrasenia)
    usu.save()
    return redirect('index.html')

def crearV (request):
    rutUsuario = request.POST.get('rutU')
    patente = request.POST.get('patente')
    marca = request.POST.get('marca')
    modelo = request.POST.get('modelo')
    anio = request.POST.get('anio')

    veh = vehiculo(rutUsuario=rutUsuario, patente=patente, marca=marca, modelo = modelo, anio=anio)
    veh.save()
    return redirect('index.html')

