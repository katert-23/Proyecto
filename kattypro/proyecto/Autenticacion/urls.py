from django.urls import path

from .views import Registros, cerrar_sesion, login,registro



urlpatterns = [
   
  
    path('',Registros.as_view(), name="Autenticacion"),

    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),

    path('login',login, name="login"),
    
    path('registro',registro, name="registro"),

    
]
