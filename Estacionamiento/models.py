from django.db import models

# Create your models here.
class DuenoE (models.Model):
    rut = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length = 100, default= "Holas123")
    cuentaB = models.CharField(max_length = 20,default= "Credito")
    edificio = models.CharField(max_length = 20, default ="1 32 A")
    piso = models.IntegerField()
    numero =  models.IntegerField()
    activo = models.BooleanField(default = False)


class Arrendatario (models.Model):
    rut = models.CharField(max_length=20)
    email = models.CharField(max_length= 50)
    nombre = models.CharField(max_length=30)
    tarjeta = models.CharField(max_length= 20)
    banco = models.CharField(max_length = 20, default="Banco estado")
    telefono = models.IntegerField()

class Vehiculo (models.Model):
    rutUsuario = models.CharField(max_length = 20)
    patente = models.CharField(max_length= 10)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length= 20 )
    anio = models.IntegerField()

class EstacionamientoActivo(models.Model):
    rutDueno = models.CharField(max_length = 20)
    direccion = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 20)
    piso = models.IntegerField()
    numero = models.IntegerField()
    precioHora = models.IntegerField()

class Boleta(models.Model):
    patenteVe = models.CharField(max_length= 10)
    codEstacionamieno = models.IntegerField()
    HoraIni = models.IntegerField()
    HoraFin =  models.IntegerField()
    valor =  models.IntegerField()