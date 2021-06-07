import requests
import respuesta
import conexion_bmp
import conexion_dynamo
import re
import settings


#-----------------------------------------------------------------------------------------------------------

def valida_dominio_usuario(fill,usuario_gestor,dominio_gestor):
    
    usuario_registrado = fill["user"]
    dominio_registrado = fill["domain"]

    if (str(dominio_gestor) == str(dominio_registrado)):
        if(usuario_gestor == usuario_registrado):
            body = respuesta.gestor_registrado(fill)
        else:
            body = respuesta.diferente_usuario(usuario_registrado)
    else:
        dominio = conexion_bmp.nombre_dominio(dominio_registrado)
        body = respuesta.diferente_dominio(dominio,usuario_registrado)
    
    return body


#-----------------------------------------------------------------------------------------------------------

def valida_estatus(fill,usuario_gestor,dominio_gestor):
    
    estatus_registrado = fill["value003"]

    if(estatus_registrado=='Activo'):
        body = valida_dominio_usuario(fill,usuario_gestor,dominio_gestor)
    else:
        body = respuesta.gestor_registrado(fill)
    
    return body

#-----------------------------------------------------------------------------------------------------------
def consulta_renapo(curp):

    print("Iniciando validacion de curp" , curp , " en renapo")
    global body
    url = "https://curp-renapo.p.rapidapi.com/v1/curp/" + curp 
    print("URL: " , url)

    querystring = {"options[rfc]":"false"}

    headers = {
        'x-rapidapi-key': settings.rapidapi_key,
        'x-rapidapi-host': "curp-renapo.p.rapidapi.com"
        }

    response_renapo = requests.request("GET", url, headers=headers, params=querystring)
    print("EL TIPO DE RESPONSE DE LA RENAPO ES: " , type(response_renapo))
    
    return response_renapo

#-----------------------------------------------------------------------------------------------------------
def respuesta_renapo(response_renapo):

    response_renapo_json = response_renapo.json()
    print("response_renapo.status_code:" , response_renapo.status_code)
    print("response_renapo_json:" ,response_renapo_json )
    print("response_renapo_json[renapo_valid]:" ,response_renapo_json["renapo_valid"] )
    if (response_renapo.status_code == 200):
        if(response_renapo_json["renapo_valid"] == True):
            conexion_dynamo.set_user_dynamo(response_renapo_json)
            body = respuesta.gestor_nuevo(response_renapo_json)
        else:
            print("El curp es invalido en la renapo")
            body = respuesta.curp_invalido()
    else:
        body = respuesta.error_servicio_renapo()
    
    return body
            

def expresion_regular_curp(curp):
    re_curp = '^[A-Za-z]{1}[AEIOUaeiouXx]{1}[A-Za-z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HMhm]{1}(AS|as|BC|bc|BS|bs|CC|cc|CS|cs|CH|ch|CL|cl|CM|cm|DF|df|DG|dg|GT|gt|GR|gr|HG|hg|JC|jc|MC|mc|MN|mn|MS|ms|NT|nt|NL|nl|OC|oc|PL|pl|QT|qt|QR|qr|SP|sp|SL|sl|SR|sr|TC|tc|TS|ts|TL|tl|VZ|vz|YN|yn|ZS|zs|NE|ne)[B-Db-dF-Hf-hJ-Nj-nP-Tp-tV-Zv-z]{3}[0-9A-Za-z]{1}[0-9]{1}'
    patron = re.compile(re_curp)

    if(patron.match(curp)):
        return True
    else:
        return False



