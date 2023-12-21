from django.shortcuts import render
from .views_marketing import *
from .views_contabilidad import *

# Create your views here.

def home(request):
    return render(request, 'Aplication/home.html')

def marketing(request):
    return render(request, 'Aplication/marketing.html')

def contabilidad(request):
    return render(request, 'Aplication/contabilidad.html')

def logistica(request):
    return render(request, 'Aplication/logistica.html')

def recursos_humanos(request):
    return render(request, 'Aplication/rrhh.html')