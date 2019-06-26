from django.contrib import admin
from django.urls import path,include
from . import views 


urlpatterns = [
    #link de navegacion 
    path('',views.index, name="index"),
    path('registro/',views.registro, name="registro"),
    path('perfil/',views.perfil, name="perfil"),
    path('disponibles/',views.disponibilidad, name="disponibilidad"),
    path('administrador', views.administrador, name="administrador"),


    #Metodos
    #pagina administrador
    path('eliminarD/<int:id>', views.eliminarD, name="eliminarD"),
    path('eliminarA/<int:id>', views.eliminarA, name="eliminarA"),
    path('eliminarV/<int:id>', views.eliminarV, name="eliminarV"),
    #dueño
    path('registro/crearD', views.crearD, name="crearD"),
    path('perfil/activar', views.activarEstacionamiento, name="activar"),
    path('perfil/desactivar/<int:rut>', views.desactivarEstacionamiento, name="desactivar"),
    #arrendador
    path('registro/crearA', views.crearA, name="crearA"),
    path('perfil/agregarV', views.crearV, name="agregarV"),
    path('perfil/eliminarV/<int:id>',views.eliminarV, name="eliminarV"),
    #Usuario
    path('eliminarU/<int:id>', views.eliminarU, name="eliminarU"),



  

]