from django.shortcuts import render

# Create your views here

def CambiarContrasenia(request):
    return render(request, 'menu/CambiarContrasenia.html')

def Camionetas(request):
    return render(request, 'menu/Camionetas.html')