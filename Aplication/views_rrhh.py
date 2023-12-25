from django.shortcuts import render
from .models import  Trabajadores
# Recursos Humanos


def alta_trabajador(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Trabajador = request.POST.get('DNI_Trabajador')
        Nombre_Trabajador = request.POST.get('Nombre')
        Telefono_trabajador = request.POST.get('Telefono_trabajador')
        
        Salario = request.POST.get('Salario')
        Domicilio = request.POST.get('Domicilio')

        # Inserta los datos en la tabla
        trabajador = Trabajadores(
            DNI_Trabajador=DNI_Trabajador,
            Nombre_Trabajador=Nombre_Trabajador,
            Telefono_trabajador=Telefono_trabajador,
           
            Salario=Salario,
            Domicilio=Domicilio
        )
        trabajador.save()

        # Redirecciona a alguna vista o página después de la inserción (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/rrhh.html')

    # Si la solicitud no es POST, renderiza el formulario de alta_trabajador
    return render(request, 'Aplication/Recursos_Humanos/alta_trabajador.html')

def trabajadores_list(request):
    trabajadores = Trabajadores.objects.all()
    return render(request, 'Aplication/Recursos_Humanos/trabajadores_list.html', {'trabajadores': trabajadores})


def baja_trabajador(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Trabajador = request.POST.get('DNI_Trabajador')

        # Busca el socio por DNI_Socio en la base de datos
        try:
            trabajador = Trabajadores.objects.get(DNI_Trabajador=DNI_Trabajador)
        except Trabajadores.DoesNotExist:
            # Puedes manejar el caso en el que el socio no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Recursos_Humanos/baja_trabajador.html')

        # Elimina el trabajador de la base de datos
        trabajador.delete()

        # Redirecciona a alguna vista o página después de la eliminación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/rrhh.html')


def selecciona_trabajador_baja(request):
    # Recupera todos los trabajadores de la base de datos
    trabajadores = Trabajadores.objects.all()

    

    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Trabajador = request.POST.get('DNI_Trabajador')

        # Busca el trabajador por DNI_Socio en la base de datos
        try:
            trabajador = Trabajadores.objects.get(DNI_Trabajador=DNI_Trabajador)
        except Trabajadores.DoesNotExist:
            # Maneja el caso en el que el socio no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Recursos_Humanos/baja_trabajador.html', {'error_message': 'El trabajador no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Recursos_Humanos/baja_trabajador.html', {'trabajador': trabajador})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_trabajador
    return render(request, 'Aplication/Recursos_Humanos/selecciona_trabajador_baja.html', {'Trabajadores': trabajadores})


def modifica_trabajador(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Trabajador = request.POST.get('DNI_Trabajador')
        Nombre_Trabajador = request.POST.get('Nombre_Trabajador')
        Telefono_trabajador = request.POST.get('Telefono_trabajador')
       
        Salario = request.POST.get('Salario')
        Domicilio = request.POST.get('Domicilio')

        try:
            trabajador = Trabajadores.objects.get(DNI_Trabajador=DNI_Trabajador)
        except Trabajadores.DoesNotExist:
            return render(request, 'Aplication/Recursos_Humanos/modifica_trabajador.html', {'error_message': 'El trabajador no existe'})

        # Modifica los datos del socio
        trabajador.Nombre_Trabajador = Nombre_Trabajador
        trabajador.Telefono_trabajador = Telefono_trabajador
        
        trabajador.Salario = Salario
        trabajador.Domicilio = Domicilio
        trabajador.save()

        # Redirecciona a la página deseada
        return render(request, 'Aplication/rrhh.html', {'success_message': '¡Trabajador modificado correctamente!'})

def selecciona_trabajador_modifica(request):
    # Recupera todos los trabajadores de la base de datos
    trabajadores = Trabajadores.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        DNI_Trabajador = request.POST.get('DNI_Trabajador')

        # Busca el trabajador por DNI_Trabajador en la base de datos
        try:
            trabajador = Trabajadores.objects.get(DNI_Trabajador=DNI_Trabajador)
        except Trabajadores.DoesNotExist:
            # Maneja el caso en el que el trabajador no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Recursos_Humanos/modifica_trabajador.html', {'error_message': 'El trabajador no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Recursos_Humanos/modifica_trabajador.html', {'trabajador': trabajador})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_trabajadores
    return render(request, 'Aplication/Recursos_Humanos/selecciona_trabajador_modifica.html', {'Trabajadores': trabajadores})
