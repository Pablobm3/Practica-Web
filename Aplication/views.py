from django.shortcuts import render
from .models import Socios, Promociona, Financia

# Create your views here.

def home(request):
    return render(request, 'Aplication/home.html')

def contacto(request):
    return render(request, 'Aplication/contacto.html')

def galeria(request):
    return render(request, 'Aplication/galeria.html')

def marketing(request):
    return render(request, 'Aplication/marketing.html')

def contabilidad(request):
    return render(request, 'Aplication/contabilidad.html')

def logistica(request):
    return render(request, 'Aplication/logistica.html')

def recursos_humanos(request):
    return render(request, 'Aplication/rrhh.html')

def consulta_marketing(request):
    if request.method == 'GET':
            # Realiza la consulta SQL
            filas = Socios.objects.all()
            return render(request, 'Aplication/resultado.html', {'filas': filas, 'tabla': Socios.__name__})

def alta_socio(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Socio = request.POST.get('DNI_Socio')
        Nombre = request.POST.get('Nombre')
        Telefono_socio = request.POST.get('Telefono_socio')
        Correo = request.POST.get('Correo')
        N_tarjeta = request.POST.get('N_tarjeta')
        Domicilio = request.POST.get('Domicilio')

        # Inserta los datos en la tabla
        socio = Socios(
            DNI_Socio=DNI_Socio,
            Nombre=Nombre,
            Telefono_socio=Telefono_socio,
            Correo=Correo,
            N_tarjeta=N_tarjeta,
            Domicilio=Domicilio
        )
        socio.save()

        # Redirecciona a alguna vista o página después de la inserción (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/home.html')

    # Si la solicitud no es POST, renderiza el formulario de alta_socio
    return render(request, 'Aplication/Marketing/alta_socio.html')

def baja_socio(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Socio = request.POST.get('DNI_Socio')

        # Busca el socio por DNI_Socio en la base de datos
        try:
            socio = Socios.objects.get(DNI_Socio=DNI_Socio)
        except Socios.DoesNotExist:
            # Puedes manejar el caso en el que el socio no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Marketing/baja_socio.html')

        # Elimina el socio de la base de datos
        socio.delete()

        # Redirecciona a alguna vista o página después de la eliminación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/home.html')

    # Si la solicitud no es POST, renderiza el formulario de baja_socio
    return render(request, 'Aplication/Marketing/baja_socio.html')

def modifica_socio(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Socio = request.POST.get('DNI_Socio')
        Nombre = request.POST.get('Nombre')
        Telefono_socio = request.POST.get('Telefono_socio')
        Correo = request.POST.get('Correo')
        N_tarjeta = request.POST.get('N_tarjeta')
        Domicilio = request.POST.get('Domicilio')

        # Busca el socio por DNI_Socio en la base de datos
        try:
            socio = Socios.objects.get(DNI_Socio=DNI_Socio)
        except Socios.DoesNotExist:
            # Puedes manejar el caso en el que el socio no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Marketing/modifica_socio.html')

        # Modifica los datos del socio
        socio.Nombre = Nombre
        socio.Telefono_socio = Telefono_socio
        socio.Correo = Correo
        socio.N_tarjeta = N_tarjeta
        socio.Domicilio = Domicilio
        socio.save()

        # Redirecciona a alguna vista o página después de la modificación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/home.html')

    # Si la solicitud no es POST, renderiza el formulario de modifica_socio
    return render(request, 'Aplication/Marketing/modifica_socio.html')