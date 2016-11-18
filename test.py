username = ''
password = ''
debug = True

from seurvalencia.picking import *
from seurvalencia.utils import services
from base64 import decodestring

print "Seur services"
services = services()
print services

with API(username, password, debug=debug) as seurvalencia_api:
    print "Test connection"
    print seurvalencia_api.test_connection()

    print "Get cities by zip"
    print seurvalencia_api.get_city('08720')

with Picking(username, password, debug=debug) as picking_api:

    print "Send a new shipment"
    data = {}

    #~ data['adn_aduana_destino'] = ''
    #~ data['adn_aduana_origen'] = ''
    #~ data['adn_tipo_mercancia'] = ''
    #~ data['adn_valor_declarado'] = ''
    #~ data['b2c_canal_preaviso1'] = ''
    #~ data['b2c_canal_preaviso2'] = ''
    #~ data['b2c_canal_preaviso3'] = ''
    #~ data['b2c_canal1'] = ''
    #~ data['b2c_canal2'] = ''
    #~ data['b2c_canal3'] = ''
    #~ data['b2c_fecha_entrega'] = ''
    #~ data['b2c_test_llegada'] = ''
    #~ data['b2c_test_preaviso'] = ''
    #~ data['b2c_test_reparto'] = ''
    #~ data['b2c_turno_reparto'] = ''
    data['blt_observaciones'] = 'Testing API Seur'
    data['blt_referencia'] = 'REF-BLT-101055'
    #~ data['cab_producto'] = ''
    #~ data['cab_servicio'] = ''
    data['csg_atencion_de'] = 'Raimon Esteve'
    #~ data['csg_ccc'] = ''
    data['csg_codigo_postal'] = '08720'
    #~ data['csg_escalera'] = ''
    data['csg_nombre'] = 'Zikzakmedia SL'
    data['csg_nombre_via'] = 'Doctor Fleming, 28'
    #~ data['csg_numero_via'] = ''
    data['csg_pais'] = 'ES'
    #~ data['csg_piso'] = ''
    data['csg_poblacion'] = 'Vilafranca del Penedes'
    #~ data['csg_puerta'] = ''
    data['csg_telefono'] = '938902108'
    #~ data['csg_tipo_numero_via'] = ''
    #~ data['csg_tipo_via'] = ''
    #~ data['exp_bultos'] = ''
    #~ data['exp_cambio'] = ''
    #~ data['exp_cde'] = ''
    #~ data['exp_portes'] = 'F'
    #~ data['exp_reembolso'] = 'F'
    #~ data['exp_seguro'] = ''
    #~ data['exp_entregar_sabado'] = ''
    #~ data['exp_lc'] = ''
    #~ data['exp_observaciones'] = ''
    #~ data['exp_peso'] = ''
    data['exp_referencia'] = 'REF-BLT-101055'
    data['exp_valor_reembolso'] = '12.34'
    #~ data['exp_valor_seguro'] = ''
    #~ data['fr_centro_logistico'] = ''
    #~ data['fr_almacenar_hasta'] = ''
    #~ data['fr_tipo_embalaje'] = ''
    #~ data['fr_almacenar_hasta'] = ''
    #~ data['fr_entrega_sabado'] = ''
    #~ data['fr_embalaje'] = ''
    #~ data['fr_etiqueta_control'] = ''
    #~ data['gs_codigo'] = ''
    #~ data['gs_codigo_centro'] = ''
    #~ data['gs_codigo_departamento'] = ''
    #~ data['gs_consolidar_pedido'] = ''
    #~ data['gs_fecha_entrega'] = ''
    #~ data['gs_hora_desde'] = ''
    #~ data['gs_hora_hasta'] = ''
    #~ data['gs_numero_pedido'] = ''
    #~ data['gs_consignatario'] = ''
    #~ data['gs_tipo_mercancia'] = ''
    #~ data['int_divisa'] = ''
    #~ data['int_famimila_mercancia'] = ''
    #~ data['int_producto_mercancia'] = ''
    #~ data['int_codigo_pais'] = ''
    #~ data['int_codigo_postal'] = ''
    #~ data['int_contracto'] = ''
    #~ data['int_extension_direccion'] = ''
    #~ data['int_telefono'] = ''
    #~ data['int_courier'] = ''
    #~ data['int_mercancia'] = ''
    #~ data['int_codigo_pais'] = ''
    #~ data['int_codigo_postal'] = ''
    #~ data['int_valor_declarado'] = ''

    reference, label, error = picking_api.create(data)

    print reference

    if error:
        print error

    file = open("/tmp/seur-valencia.txt", "w")
    file.write(label)
    file.close()
    print "Generated label file in /tmp/seur-valencia.txt"

    print "Picking PDF deliveried"
    pdf = picking_api.info()
    file = open("/tmp/seur-valencia.pdf", "w")
    file.write(pdf)
    file.close()
    print "Generated PDF deliveries in /tmp/seur-valencia.pdf"
