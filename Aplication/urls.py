from django.urls import path
from .views import home
from .views import marketing, contabilidad, logistica, recursos_humanos
from .views import alta_socio, baja_socio, consulta_marketing, modifica_socio, selecciona_socio_baja, selecciona_socio_modifica
from .views import alta_campana, baja_campana, consulta_campana, modifica_campana, selecciona_campana_modifica, selecciona_campana_baja

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
    path('alta_campana/', alta_campana, name="alta_campana"),
    path('baja_campana/', baja_campana, name="baja_campana"),
    path('consulta_campana/', consulta_campana, name="consulta_campana"),
    path('modifica_campana/', modifica_campana, name="modifica_campana"),
    path('selecciona_socio_baja/', selecciona_socio_baja, name="selecciona_socio_baja"),
    path('selecciona_socio_modifica/', selecciona_socio_modifica, name="selecciona_socio_modifica"),
    path('selecciona_campana_modifica/', selecciona_campana_modifica, name="selecciona_campana_modifica"),
    path('selecciona_campana_baja/', selecciona_campana_baja, name="selecciona_campana_baja"),
]