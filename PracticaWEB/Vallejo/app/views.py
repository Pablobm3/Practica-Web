from django.shortcuts import render

# Create your views here.
# Por cada página que tengamos crearemos/definiremos una vista.

def home(request):
    return render(request,'app/home.html')

def articulos(request):
    return render(request, 'app/articulos.html')

def contacto(request):
    return render(request, 'app/contacto.html')

# Más adelante accederemos desde aquí a la base de datos.