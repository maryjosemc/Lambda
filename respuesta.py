import datetime



#-----------------------------------------------------------------------------------------------------------

def gestor_nuevo(response):

    fecha_nacimiento = datetime.datetime.strptime(response["birthdate"], "%d/%m/%Y").strftime("%Y-%m-%d")
    body={
            'apellido_paterno': response["paternal_surname"],
            'apellido_materno': response["mothers_maiden_name"],
            'nombre': response["names"],
            'sexo': response["sex"], 
            'fecha_nacimiento' : fecha_nacimiento,
            'entidad_nacimiento': response["probation_document_data"]["claveEntidadRegistro"],
            'unicidad': 0
    }
    return body

#-----------------------------------------------------------------------------------------------------------

def gestor_registrado_dynamo(response):

    body={
            'apellido_paterno': response["Item"]["apellido_paterno"],
            'apellido_materno': response["Item"]["apellido_materno"],
            'nombre': response["Item"]["nombre"],
            'sexo': response ["Item"]["sexo"], 
            'fecha_nacimiento' : response["Item"]["fecha_nacimiento"],
            'entidad_nacimiento': response["Item"]["entidad_nacimiento"],
            'unicidad': 0
    }
    return body

#-----------------------------------------------------------------------------------------------------------
def diferente_dominio(dominio, usuario_registrado):
        body = {"unicidad" : 1,
                "dominio_previo": dominio,
                "name_user": usuario_registrado
                }
        return body

#-----------------------------------------------------------------------------------------------------------
def diferente_usuario(usuario_registrado):
        body = {"unicidad" : 2,
                "name_user": usuario_registrado,
                #,'curp': ''
                }
        return body

#-----------------------------------------------------------------------------------------------------------

def gestor_registrado(fill):
    print("Entra a llena campos gestor registrado")
    body={
            'rfc': fill["value011"], 
            #'validacion_curp': fill["value002"], 
            'nombre': fill["value005"], 
            'apellido_paterno': fill["value006"], 
            'apellido_materno': fill["value007"], 
            'sexo': fill["value008"], 
            'fecha_nacimiento': fill["value009"], 
            'entidad_nacimiento': fill["value010"] , 
            'name_user' : fill['user'],
            "unicidad" : 0,
    }
    return body


#-----------------------------------------------------------------------------------------------------------
def curp_invalido():
        body={"unicidad": 3}
        return body

#-----------------------------------------------------------------------------------------------------------
def error_servicio_renapo():
        body = { "unicidad": 4}
        return body

#-----------------------------------------------------------------------------------------------------------
def formato_curp_invalido():
        body = {"unicidad": 5}
        return body

#-----------------------------------------------------------------------------------------------------------


