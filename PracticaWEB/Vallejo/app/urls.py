from django.urls import path
from .views import home, articulos, contacto

# Crearemos una url por cada view que tengamos (los importaremos)

urlpatterns = [
    # en la raiz (localhost:8000), se va a cargar lo que haya en el view 'home.html', y lo llamaremos "home"
    path('', home, name="home"),
    # Añadiré cada ruta que quiera que exista
    path('articulos/', articulos, name="articulos"),
    path('contacto/' , contacto, name="contacto"),
]