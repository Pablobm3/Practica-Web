from django.shortcuts import render
from .models import Socios, Campanas

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

def consulta_marketing(request):
    if request.method == 'GET':
            # Realiza la consulta SQL
            filas = Socios.objects.all()
            return render(request, 'Aplication/Marketing/resultado_marketing.html', {'filas': filas, 'tabla': Socios.__name__})

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
        return render(request, 'Aplication/marketing.html')

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
        return render(request, 'Aplication/marketing.html')

    # Si la solicitud no es POST, renderiza el formulario de baja_socio
    return render(request, 'Aplication/Marketing/baja_socio.html')

def selecciona_socio_modifica(request):
    # Recupera todos los socios de la base de datos
    socios = Socios.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Socio = request.POST.get('DNI_Socio')

        # Busca el socio por DNI_Socio en la base de datos
        try:
            socio = Socios.objects.get(DNI_Socio=DNI_Socio)
        except Socios.DoesNotExist:
            # Maneja el caso en el que el socio no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Marketing/modifica_socio.html', {'error_message': 'El socio no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Marketing/modifica_socio.html', {'socio': socio})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_socios
    return render(request, 'Aplication/Marketing/selecciona_socio_modifica.html', {'Socios': socios})

def selecciona_socio_baja(request):
    # Recupera todos los socios de la base de datos
    socios = Socios.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Socio = request.POST.get('DNI_Socio')

        # Busca el socio por DNI_Socio en la base de datos
        try:
            socio = Socios.objects.get(DNI_Socio=DNI_Socio)
        except Socios.DoesNotExist:
            # Maneja el caso en el que el socio no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Marketing/baja_socio.html', {'error_message': 'El socio no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Marketing/baja_socio.html', {'socio': socio})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_socios
    return render(request, 'Aplication/Marketing/selecciona_socio_baja.html', {'Socios': socios})

def modifica_socio(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Socio = request.POST.get('DNI_Socio')
        Nombre = request.POST.get('Nombre')
        Telefono_socio = request.POST.get('Telefono_socio')
        Correo = request.POST.get('Correo')
        N_tarjeta = request.POST.get('N_tarjeta')
        Domicilio = request.POST.get('Domicilio')

        try:
            socio = Socios.objects.get(DNI_Socio=DNI_Socio)
        except Socios.DoesNotExist:
            return render(request, 'Aplication/Marketing/modifica_socio.html', {'error_message': 'El socio no existe'})

        # Modifica los datos del socio
        socio.Nombre = Nombre
        socio.Telefono_socio = Telefono_socio
        socio.Correo = Correo
        socio.N_tarjeta = N_tarjeta
        socio.Domicilio = Domicilio
        socio.save()

        # Redirecciona a la página deseada
        return render(request, 'Aplication/marketing.html')



def alta_campana(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Campana = request.POST.get('ID_Campana')
        Nom_Campana = request.POST.get('Nom_Campana')
        Tipo = request.POST.get('Tipo')
        Duracion = request.POST.get('Duracion')
        Presupuesto = request.POST.get('Presupuesto')

        # Inserta los datos en la tabla
        campana = Campanas(
            ID_Campana=ID_Campana,
            Nom_Campana=Nom_Campana,
            Tipo=Tipo,
            Duracion=Duracion,
            Presupuesto=Presupuesto
        )
        campana.save()

        # Redirecciona a alguna vista o página después de la inserción (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/marketing.html')

    # Si la solicitud no es POST, renderiza el formulario de alta_campana
    return render(request, 'Aplication/Marketing/alta_campana.html')

def baja_campana(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Campana = request.POST.get('ID_Campana')

        # Busca la campaña por ID_Campana en la base de datos
        try:
            campana = Campanas.objects.get(ID_Campana=ID_Campana)
        except Campanas.DoesNotExist:
            # Puedes manejar el caso en el que la campaña no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Marketing/baja_campana.html')

        # Elimina la campaña de la base de datos
        campana.delete()

        # Redirecciona a alguna vista o página después de la eliminación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/marketing.html')

    # Si la solicitud no es POST, renderiza el formulario de baja_campana
    return render(request, 'Aplication/Marketing/baja_campana.html')

def selecciona_campana_modifica(request):
    # Recupera todas las campañas de la base de datos
    campanas = Campanas.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Campana = request.POST.get('ID_Campana')

        # Busca la campaña por ID_Campana en la base de datos
        try:
            campana = Campanas.objects.get(ID_Campana=ID_Campana)
        except Campanas.DoesNotExist:
            # Maneja el caso en el que la campaña no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Marketing/modifica_campana.html', {'error_message': 'La campaña no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        # Si se llama desde modifica_campana, redirige a modifica_campana
        # Si se llama desde baja_campana, redirige a baja_campana
        return render(request, 'Aplication/Marketing/modifica_campana.html', {'campana': campana})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_campana
    return render(request, 'Aplication/Marketing/selecciona_campana_modifica.html', {'Campanas': campanas})

def selecciona_campana_baja(request):
    # Recupera todas las campañas de la base de datos
    campanas = Campanas.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Campana = request.POST.get('ID_Campana')

        # Busca la campaña por ID_Campana en la base de datos
        try:
            campana = Campanas.objects.get(ID_Campana=ID_Campana)
        except Campanas.DoesNotExist:
            # Maneja el caso en el que la campaña no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Marketing/baja_campana.html', {'error_message': 'La campaña no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        # Si se llama desde modifica_campana, redirige a modifica_campana
        # Si se llama desde baja_campana, redirige a baja_campana
        return render(request, 'Aplication/Marketing/baja_campana.html', {'campana': campana})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_campana
    return render(request, 'Aplication/Marketing/selecciona_campana_baja.html', {'Campanas': campanas})

def modifica_campana(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Campana = request.POST.get('ID_Campana')
        Nom_Campana = request.POST.get('Nom_Campana')
        Tipo = request.POST.get('Tipo')
        Duracion = request.POST.get('Duracion')
        Presupuesto = request.POST.get('Presupuesto')

        # Busca la campaña por ID_Campana en la base de datos
        try:
            campana = Campanas.objects.get(ID_Campana=ID_Campana)
        except Campanas.DoesNotExist:
            # Puedes manejar el caso en el que la campaña no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Marketing/modifica_campana.html')

        # Modifica los datos de la campaña
        if Nom_Campana.strip() != '':
            campana.Nom_Campana = Nom_Campana
        if Tipo.strip() != '':
            campana.Tipo = Tipo
        if Duracion.strip() != '':
            campana.Duracion = Duracion
        if Presupuesto.strip() != '':
            campana.Presupuesto = Presupuesto
        
        campana.save()

        # Redirecciona a alguna vista o página después de la modificación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/marketing.html')

    # Si la solicitud no es POST, renderiza el formulario de modifica_campana
    return render(request, 'Aplication/Marketing/modifica_campana.html')

def consulta_campana(request):
    if request.method == 'GET':
            # Realiza la consulta SQL
            filas = Campanas.objects.all()
            return render(request, 'Aplication/Marketing/resultado_marketing.html', {'filas': filas, 'tabla': Campanas.__name__})