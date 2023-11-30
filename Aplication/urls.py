from django.urls import path
from .views import home
from .views import marketing, contabilidad, logistica, recursos_humanos
from .views import alta_socio, baja_socio, consulta_marketing, modifica_socio

urlpatterns = [
    path('', home, name='home'),
    path('marketing/', marketing, name="marketing"),
    path('contabilidad/', contabilidad, name="contabilidad"),
    path('logistica/', logistica, name="logistica"),
    path('rrhh/', recursos_humanos, name="rrhh"),
    path('alta_socio/', alta_socio, name="alta_socio"),
    path('baja_socio/', baja_socio, name="baja_socio"),
    path('consulta_marketing/', consulta_marketing, name="consulta_marketing"),
    path('modifica_socio/', modifica_socio, name="modifica_socio"),

]