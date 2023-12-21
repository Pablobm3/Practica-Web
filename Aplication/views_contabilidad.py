from django.shortcuts import render
from .models import Gastos, Ingreso_factura

# Contabilidad
def alta_gasto(request):
    if request.method == 'POST':
        ID_gasto = request.POST.get('ID_gasto')
        Cantidad = request.POST.get('Cantidad')
        Tipo_gasto = request.POST.get('Tipo_gasto')
        gasto = Gastos(ID_gasto = ID_gasto, Cantidad = Cantidad, Tipo_gasto = Tipo_gasto)
        gasto.save()

        return render(request,'Aplication/contabilidad.html')

    return render(request,'Aplication/Contabilidad/alta_gasto.html')

def alta_ingreso_factura(request):
    if request.method == 'POST':
        ID_ingreso = request.POST.get('ID_ingreso')
        Cantidad = request.POST.get('Cantidad')
        Tipo_gasto = request.POST.get('Tipo_gasto')
        DNI_Socio = request.POST.get('DNI_Socio')
        ID_Articulo = request.POST.get('ID_Articulo')
        Fecha_factura = request.POST.get('Fecha_factura')
        ingreso_factura = Ingreso_factura(ID_ingreso = ID_ingreso, Cantidad = Cantidad, Tipo_gasto = Tipo_gasto, DNI_Socio = DNI_Socio, ID_Articulo = ID_Articulo, Fecha_factura = Fecha_factura)
        ingreso_factura.save()

        return render(request,'Aplication/contabilidad.html')

    return render(request,'Aplication/Contabilidad/alta_ingreso_factura.html')

def baja_gasto(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_gasto = request.POST.get('ID_gasto')

        # Busca el gasto por ID_gasto en la base de datos
        try:
            gasto = Gastos.objects.get(ID_gasto=ID_gasto)
        except Gastos.DoesNotExist:
            # Puedes manejar el caso en el que el gasto no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Contabilidad/baja_gasto.html')

        # Elimina el gasto de la base de datos
        gasto.delete()

        # Redirecciona a alguna vista o página después de la eliminación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/contabilidad.html')

    # Si la solicitud no es POST, renderiza el formulario de baja_gasto
    return render(request, 'Aplication/Contabilidad/baja_gasto.html')

def baja_ingreso_factura(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_ingreso = request.POST.get('ID_ingreso')

        # Busca el gasto por ID_gasto en la base de datos
        try:
            ingreso_factura = Ingreso_factura.objects.get(ID_ingreso=ID_ingreso)
        except Ingreso_factura.DoesNotExist:
            # Puedes manejar el caso en el que el gasto no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Contabilidad/baja_ingreso_factura.html')

        # Elimina el gasto de la base de datos
        ingreso_factura.delete()

        # Redirecciona a alguna vista o página después de la eliminación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/contabilidad.html')

    # Si la solicitud no es POST, renderiza el formulario de baja_gasto
    return render(request, 'Aplication/Contabilidad/baja_ingreso_factura.html')  

def consulta_gastos(request):
    if request.method == 'GET':
            # Realiza la consulta SQL
            filas = Gastos.objects.all()
            return render(request, 'Aplication/Contabilidad/resultado_contabilidad.html', {'filas': filas, 'tabla': Gastos.__name__})
    
def consulta_ingreso_factura(request):
    if request.method == 'GET':
        # Realiza la consulta SQL
        filas = Ingreso_factura.objects.all()
        return render(request, 'Aplication/Contabilidad/resultado_contabilidad.html', {'filas': filas, 'tabla': Ingreso_factura.__name__})
    
def modifica_gasto(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_gasto = request.POST.get('ID_gasto')
        Cantidad = request.POST.get('Cantidad')
        Tipo_gasto = request.POST.get('Tipo_gasto')

        # Busca la campaña por ID_gasto en la base de datos
        try:
            gasto = Gastos.objects.get(ID_gasto=ID_gasto)
        except Gastos.DoesNotExist:
            # Puedes manejar el caso en el que la campaña no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Contabilidad/modifica_gasto.html')

        # Modifica los datos de la campaña
        if Cantidad.strip() != '':
            gasto.Cantidad = Cantidad
        if Tipo_gasto.strip() != '':
            gasto.Tipo_gasto = Tipo_gasto

        gasto.save()

        # Redirecciona a alguna vista o página después de la modificación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/contabilidad.html')

    # Si la solicitud no es POST, renderiza el formulario de modifica_campana
    return render(request, 'Aplication/Contabilidad/modifica_gasto.html')

def selecciona_gasto_modifica(request):
    # Recupera todos los gastos de la base de datos
    gastos = Gastos.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_gasto = request.POST.get('ID_gasto')

        # Busca el socio por ID_gasto en la base de datos
        try:
            gasto = Gastos.objects.get(ID_gasto=ID_gasto)
        except Gastos.DoesNotExist:
            # Maneja el caso en el que el gasto no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Contabilidad/modifica_gasto.html', {'error_message': 'El gasto no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Contabilidad/modifica_gasto.html', {'gasto': gasto})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_gastos
    return render(request, 'Aplication/Contabilidad/selecciona_gasto_modifica.html', {'Gastos': gastos})

def modifica_ingreso_factura(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_ingreso = request.POST.get('ID_ingreso')
        Cantidad = request.POST.get('Cantidad')
        Tipo_gasto = request.POST.get('Tipo_gasto')
        DNI_Socio = request.POST.get('DNI_Socio')
        ID_Articulo = request.POST.get('ID_Articulo')
        Fecha_factura = request.POST.get('Fecha_factura')

        # Busca la campaña por ID_gasto en la base de datos
        try:
            ingreso = Ingreso_factura.objects.get(ID_ingreso=ID_ingreso)
        except Ingreso_factura.DoesNotExist:
            # Puedes manejar el caso en el que la campaña no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Contabilidad/modifica_ingreso_factura.html')

        # Modifica los datos de la campaña
        if Cantidad.strip() != '':
            ingreso.Cantidad = Cantidad
        if Tipo_gasto.strip() != '':
            ingreso.Tipo_gasto = Tipo_gasto
        if DNI_Socio.strip() != '':
            ingreso.DNI_Socio = DNI_Socio
        if ID_Articulo.strip() != '':
            ingreso.ID_Articulo = ID_Articulo
        if Fecha_factura.strip() != '':
            ingreso.Fecha_factura = Fecha_factura

        ingreso.save()

        # Redirecciona a alguna vista o página después de la modificación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/contabilidad.html')

    # Si la solicitud no es POST, renderiza el formulario de modifica_campana
    return render(request, 'Aplication/Contabilidad/modifica_ingreso_factura.html')

def selecciona_ingreso_factura_modifica(request):
    # Recupera todos los gastos de la base de datos
    ingresos = Ingreso_factura.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_ingreso = request.POST.get('ID_ingreso')

        # Busca el socio por ID_gasto en la base de datos
        try:
            ingreso = Ingreso_factura.objects.get(ID_ingreso=ID_ingreso)
        except Ingreso_factura.DoesNotExist:
            # Maneja el caso en el que el gasto no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Contabilidad/modifica_ingreso_factura.html', {'error_message': 'El ingreso no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Contabilidad/modifica_ingreso_factura.html', {'ingreso': ingreso})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_gastos
    return render(request, 'Aplication/Contabilidad/selecciona_ingreso_factura_modifica.html', {'Ingreso_factura': ingresos})

def selecciona_gasto_baja(request):
    # Recupera todas las campañas de la base de datos
    gastos = Gastos.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_gasto = request.POST.get('ID_gasto')

        # Busca la campaña por ID_Campana en la base de datos
        try:
            gasto = Gastos.objects.get(ID_gasto=ID_gasto)
        except Gastos.DoesNotExist:
            # Maneja el caso en el que la campaña no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Contabilidad/baja_gasto.html', {'error_message': 'El gasto no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        # Si se llama desde modifica_campana, redirige a modifica_campana
        # Si se llama desde baja_campana, redirige a baja_campana
        return render(request, 'Aplication/Contabilidad/baja_gasto.html', {'gasto': gasto})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_campana
    return render(request, 'Aplication/Contabilidad/selecciona_gasto_baja.html', {'Gastos': gastos})

def selecciona_ingreso_factura_baja(request):
    # Recupera todos los ingresos de la base de datos
    ingresos = Ingreso_factura.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_ingreso = request.POST.get('ID_ingreso')

        # Busca la campaña por ID_Campana en la base de datos
        try:
            ingreso = Ingreso_factura.objects.get(ID_ingreso=ID_ingreso)
        except Ingreso_factura.DoesNotExist:
            # Maneja el caso en el que no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Contabilidad/baja_ingreso_factura.html', {'error_message': 'El ingreso de factura no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Contabilidad/baja_ingreso_factura.html', {'ingreso': ingreso})

    # Si la solicitud no es POST, renderiza el formulario
    return render(request, 'Aplication/Contabilidad/selecciona_ingreso_factura_baja.html', {'Ingreso_factura': ingresos})