from django.shortcuts import render
from .models import Articulos, Proveedor, Compra

#Logistica

'''
def logistica(request):
    return render(request, 'Aplication/logistica.html')
'''

''' -------------------------- '''
''' VISTAS ALBERTO - LOGISTICA '''
''' -------------------------- '''

def consulta_articulo(request):
    if request.method == 'GET':
            # Realiza la consulta SQL
            filas = Articulos.objects.all()
            return render(request, 'Aplication/Logistica/resultado_logistica.html', {'filas': filas, 'tabla': Articulos.__name__})

def consulta_proveedor(request):
    if request.method == 'GET':
            # Realiza la consulta SQL
            filas = Proveedor.objects.all()
            return render(request, 'Aplication/Logistica/resultado_logistica.html', {'filas': filas, 'tabla': Proveedor.__name__})
    
def alta_proveedor(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        Nompro = request.POST.get('Nompro')
        Deporte_especializado = request.POST.get('Deporte_especializado')
        Ciudad = request.POST.get('Ciudad')
        Telefono_proveedor = request.POST.get('Telefono_proveedor')

        # Verifica si ya existe un proveedor con el mismo Nompro
        try:
            existe_proveedor = Proveedor.objects.get(Nompro=Nompro)
            # Si ya existe, muestra un mensaje de error o realiza la acción deseada
            return render(request, 'Aplication/Logistica/alta_proveedor.html', {'error_message': '¡Ya existe un proveedor con el mismo DNI!'})
        except Proveedor.DoesNotExist:
        # Inserta los datos en la tabla
            proveedor = Proveedor(
                Nompro=Nompro,
                Deporte_especializado=Deporte_especializado,
                Ciudad=Ciudad,
                Telefono_proveedor=Telefono_proveedor,
            )
            proveedor.save()

            # Redirecciona a alguna vista o página después de la inserción (puedes cambiar 'home' a la URL deseada)
            return render(request, 'Aplication/logistica.html',{'success_message': '¡Proveedor registrado correctamente!'})

    # Si la solicitud no es POST, renderiza el formulario de alta_proveedor
    return render(request, 'Aplication/logistica/alta_proveedor.html')

def baja_proveedor(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        Nompro = request.POST.get('Nompro')

        # Busca el proveedor por Nompro en la base de datos
        try:
            proveedor = Proveedor.objects.get(Nompro=Nompro)
        except Proveedor.DoesNotExist:
            # Puedes manejar el caso en el que el proveedor no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/logistica/baja_proveedor.html')

        # Elimina el proveedor de la base de datos
        proveedor.delete()

        # Redirecciona a alguna vista o página después de la eliminación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/logistica.html', {'success_message': 'Proveedor eliminado correctamente!'})

    # Si la solicitud no es POST, renderiza el formulario de baja_proveedor
    return render(request, 'Aplication/logistica/baja_proveedor.html')

def selecciona_proveedor_baja(request):
    # Recupera todos los provedores de la base de datos
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        Nompro = request.POST.get('Nompro')

        # Busca el proveedor por Nompro en la base de datos
        try:
            proveedor = Proveedor.objects.get(Nompro=Nompro)
        except Proveedor.DoesNotExist:
            # Maneja el caso en el que el proveedor no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Logistica/baja_proveedor.html', {'error_message': 'El proveedor no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Logistica/baja_proveedor.html', {'proveedor': proveedor})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_proveedor
    return render(request, 'Aplication/Logistica/selecciona_proveedor_baja.html' , {'Proveedor': proveedores})

def alta_articulo(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Articulo = request.POST.get('ID_Articulo')
        Cantidad = request.POST.get('Cantidad')
        Precio = request.POST.get('Precio')
        Deporte = request.POST.get('Deporte')

        # Verifica si ya existe un artículo con el mismo ID_Articulo
        try:
            existe_articulo = Articulos.objects.get(ID_Articulo=ID_Articulo)
            # Si ya existe, muestra un mensaje de error o realiza la acción deseada
            return render(request, 'Aplication/Logistica/alta_articulo.html', {'error_message': '¡Ya existe un artículo con el mismo ID!'})
        except Articulos.DoesNotExist:
            # Inserta los datos en la tabla
            articulo = Articulos(
                ID_Articulo=ID_Articulo,
                Cantidad=Cantidad,
                Precio=Precio,
                Deporte=Deporte,
            )
            articulo.save()

            # Redirecciona a alguna vista o página después de la inserción (puedes cambiar 'home' a la URL deseada)
            return render(request, 'Aplication/logistica.html', {'success_message': '¡Artículo registrado correctamente!'})

    # Si la solicitud no es POST, renderiza el formulario de alta_articulo
    return render(request, 'Aplication/Logistica/alta_articulo.html')

def baja_articulo(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Articulo = request.POST.get('ID_Articulo')

        # Busca el articulo por ID_Articulo en la base de datos
        try:
            articulo = Articulos.objects.get(ID_Articulo=ID_Articulo)
        except Articulos.DoesNotExist:
            # Puedes manejar el caso en el que el artículo no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Logistica/baja_articulo.html')

        # Elimina el artículo de la base de datos
        articulo.delete()

        # Redirecciona a alguna vista o página después de la eliminación (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/logistica.html', {'success_message': '¡Artículo eliminado correctamente!'})

    # Si la solicitud no es POST, renderiza el formulario de baja_articulo
    return render(request, 'Aplication/Logistica/baja_articulo.html')

def selecciona_articulo_baja(request):
    # Recupera todos los artículos de la base de datos
    articulos = Articulos.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Articulo = request.POST.get('ID_Articulo')

        # Busca el articulo por ID_Articulo en la base de datos
        try:
            articulo = Articulos.objects.get(ID_Articulo=ID_Articulo)
        except Articulos.DoesNotExist:
            # Maneja el caso en el que el artículo no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Logistica/baja_articulo.html', {'error_message': 'El articulo no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Logistica/baja_articulo.html', {'articulo': articulo})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_articulo
    return render(request, 'Aplication/Logistica/selecciona_articulo_baja.html', {'Articulos': articulos})

def modifica_proveedor(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        Nompro = request.POST.get('Nompro')
        Deporte_especializado = request.POST.get('Deporte_especializado')
        Ciudad = request.POST.get('Ciudad')
        Telefono_proveedor = request.POST.get('Telefono_proveedor')

        try:
            proveedor = Proveedor.objects.get(Nompro=Nompro)
        except Proveedor.DoesNotExist:
            return render(request, 'Aplication/Logistica/modifica_proveedor.html', {'error_message': 'El proveedor no existe'})

        # Modifica los datos del proveedor
        proveedor.Deporte_especializado = Deporte_especializado
        proveedor.Ciudad = Ciudad
        proveedor.Telefono_proveedor = Telefono_proveedor
        proveedor.save()
        
        # Redirecciona a la página deseada
        return render(request, 'Aplication/logistica.html', {'success_message': '¡Proveedor modificado correctamente!'})
    
    # Si la solicitud no es POST, renderiza el formulario de modifica_proveedor
    # return render(request, 'Aplication/Logistica/modifica_proveedor.html')

def selecciona_proveedor_modifica(request):
    # Recupera todos los proveedores de la base de datos
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        Nompro = request.POST.get('Nompro')

        # Busca la el proveedor por Nompro en la base de datos
        try:
            proveedor = Proveedor.objects.get(Nompro=Nompro)
        except Proveedor.DoesNotExist:
            # Maneja el caso en el que el articulo no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Logistca/modifica_proveedor.html', {'error_message': 'El proveedor no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        return render(request, 'Aplication/Logistica/modifica_proveedor.html', {'proveedor': proveedor})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_proveedor
    return render(request, 'Aplication/Logistica/selecciona_proveedor_modifica.html', {'Proveedor': proveedores})

def modifica_articulo(request):
    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Articulo = request.POST.get('ID_Articulo')
        Cantidad = request.POST.get('Cantidad')
        Precio = request.POST.get('Precio')
        Deporte = request.POST.get('Deporte')
    
        # Busca el artículo por ID_Articulo en la base de datos
        try:
            articulo = Articulos.objects.get(ID_Articulo=ID_Articulo)
        except Articulos.DoesNotExist:
            # Puedes manejar el caso en el que el articulo no existe
            # Manda un mensaje de error
            return render(request, 'Aplication/Logistica/modifica_articulo.html')

        # Modifica los datos del artículo
        if Cantidad.strip() != '':
            articulo.Cantidad = Cantidad
        if Precio.strip() != '':
            articulo.Tipo = Precio
        if Deporte.strip() != '':
            articulo.Duracion = Deporte

        articulo.save()

        # Redirecciona a la página deseada
        return render(request, 'Aplication/logistica.html', {'success_message': '¡Artículo modificado correctamente!'})
    
    # Si la solicitud no es POST, renderiza el formulario de modifica_articulo
    return render(request, 'Aplication/Logistica/modifica_articulo.html')

def selecciona_articulo_modifica(request):
    # Recupera todos los artículos de la base de datos
    articulos = Articulos.objects.all()

    if request.method == 'POST':
        # Recoge los datos del formulario
        ID_Articulo = request.POST.get('ID_Articulo')

        # Busca la el artículo por ID_Articulo en la base de datos
        try:
            articulo = Articulos.objects.get(ID_Articulo=ID_Articulo)
        except Articulos.DoesNotExist:
            # Maneja el caso en el que el articulo no existe
            # Muestra un mensaje de error en el formulario o redirige a alguna página
            return render(request, 'Aplication/Logistca/modifica_articulo.html', {'error_message': 'El articulo no existe'})

        # Redirige a la página deseada después de la selección (puedes cambiar 'home' a la URL deseada)
        # Si se llama desde modifica_articulo, redirige a modifica_articulo
        # Si se llama desde baja_articulo, redirige a baja_articulo
        return render(request, 'Aplication/Logistica/modifica_articulo.html', {'articulo': articulo})

    # Si la solicitud no es POST, renderiza el formulario de selecciona_articulo
    return render(request, 'Aplication/Logistica/selecciona_articulo_modifica.html', {'Articulos': articulos})