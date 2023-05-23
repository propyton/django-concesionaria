"""concesionaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import Camionetas, CambiarContrasenia, FordF150Platinum, FordF150Raptor, InicioDesesion, jeep, Mazda, MenuPrincipal, PerfilDeUsuario, portada, RegistroDeUsuario, Silverado, subaru, Suv

urlpatterns = [
   path('',Camionetas, name="Camionetas"),
   path('Cambiar', CambiarContrasenia, name="CambiarContrasenia"),
   path('FordF150Platinum', FordF150Platinum, name="FordF150Platinum"),
   path('FordF150Raptor', FordF150Raptor, name="FordF150Raptor"),
   path('InicioDesesion', InicioDesesion, name="InicioDesesion"),
   path('jeep', jeep, name="jeep"),
   path('Mazda', Mazda, name="Mazda"),
   path('MenuPrincipal', MenuPrincipal, name="MenuPrincipal"),
   path('PerfilDeUsuario', PerfilDeUsuario, name="PerfilDeUsuario"),
   path('portada', portada, name="portada"),
   path('RegistroDeUsuario', RegistroDeUsuario, name="RegistroDeUsuario"),
   path('Silverado', Silverado, name="Silverado"),
   path('subaru', subaru, name="subaru"),
   path('Suv', Suv, name="Suv"),
   
]