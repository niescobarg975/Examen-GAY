from django.contrib import admin
from django.urls import path,include
from . import views 


urlpatterns = [
    #link de navegacion 
    path('',views.index, name="index"),
    path('registro/',views.registro, name="registro"),
]