from django.urls import path
from .views import home
from .views import marketing, contabilidad, logistica, recursos_humanos

from .views import alta_socio, baja_socio, consulta_marketing, modifica_socio, selecciona_socio_baja, selecciona_socio_modifica
from .views import alta_campana, baja_campana, consulta_campana, modifica_campana, selecciona_campana_modifica, selecciona_campana_baja

from .views import alta_gasto, baja_gasto, consulta_gastos, modifica_gasto, selecciona_gasto_modifica, selecciona_gasto_baja
from .views import alta_ingreso_factura, baja_ingreso_factura, consulta_ingreso_factura, modifica_ingreso_factura, selecciona_ingreso_factura_modifica, selecciona_ingreso_factura_baja

''' Imports Alberto - Logistica'''
from .views import alta_articulo, alta_proveedor, baja_articulo, baja_proveedor, consulta_articulo, consulta_proveedor
from .views import modifica_articulo, modifica_proveedor
from .views import selecciona_articulo_baja, selecciona_articulo_modifica, selecciona_proveedor_baja, selecciona_proveedor_modifica

urlpatterns = [
    path('', home, name='home'),
    path('marketing/', marketing, name="marketing"),
    path('contabilidad/', contabilidad, name="contabilidad"),
    path('logistica/', logistica, name="logistica"),
    path('rrhh/', recursos_humanos, name="rrhh"),
  
    #FRANCISCO
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
    
    #ANTONIO
    path('alta_gasto/', alta_gasto, name = "alta_gasto"),
    path('alta_ingreso_factura', alta_ingreso_factura, name = "alta_ingreso_factura"),
    path('baja_gasto', baja_gasto, name = "baja_gasto"),
    path('baja_ingreso_factura', baja_ingreso_factura, name = "baja_ingreso_factura"),
    path('consulta_gastos', consulta_gastos, name = "consulta_gastos"),
    path('consulta_ingreso_factura', consulta_ingreso_factura, name = "consulta_ingreso_factura"),
    path('modifica_gasto', modifica_gasto, name = "modifica_gasto"),
    path('selecciona_gasto_modifica', selecciona_gasto_modifica, name = "selecciona_gasto_modifica"),
    path('modifica_ingreso_factura', modifica_ingreso_factura, name = "modifica_ingreso_factura"),
    path('selecciona_ingreso_factura_modifica',selecciona_ingreso_factura_modifica ,name = "selecciona_ingreso_factura_modifica"),
    path('selecciona_gasto_baja', selecciona_gasto_baja, name = "selecciona_gasto_baja"),
    path('selecciona_ingreso_factura_baja', selecciona_ingreso_factura_baja, name = "selecciona_ingreso_factura_baja"),

    #ALBERTO
    path('logistica/', logistica, name="logistica"),
    path('alta_proveedor/', alta_proveedor, name="alta_proveedor"),
    path('baja_proveedor/', baja_proveedor, name="baja_proveedor"),
    path('consulta_proveedor/', consulta_proveedor, name="consulta_proveedor"),
    path('modifica_proveedor/', modifica_proveedor, name="modifica_proveedor"),
    path('alta_articulo/', alta_articulo, name="alta_articulo"),
    path('baja_articulo/', baja_articulo, name="baja_articulo"),
    path('consulta_articulo/', consulta_articulo, name="consulta_articulo"),
    path('modifica_articulo/', modifica_articulo, name="modifica_articulo"),
    path('selecciona_proveedor_baja/', selecciona_proveedor_baja, name="selecciona_proveedor_baja"),
    path('selecciona_proveedor_modifica/', selecciona_proveedor_modifica, name="selecciona_proveedor_modifica"),
    path('selecciona_articulo_modifica/', selecciona_articulo_modifica, name="selecciona_articulo_modifica"),
    path('selecciona_articulo_baja/', selecciona_articulo_baja, name="selecciona_articulo_baja"),

]