
import boto3
import respuesta
import validaciones
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('curps_unicos')


def get_user_dynamo(curp):
    
 
    try:
        
        table = dynamodb.Table('curps_unicos')
        response = table.get_item(Key={'curp': "baz_" + curp},ConsistentRead=True)
    
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        if 'Item' not in response:
            response_renapo = validaciones.consulta_renapo(curp)
            body = validaciones.respuesta_renapo(response_renapo)
        else:
            body = respuesta.gestor_registrado_dynamo(response)

        
    return body

def set_user_dynamo(response_renapo_json):
    
    fecha_nacimiento = datetime.datetime.strptime(response_renapo_json["birthdate"], "%d/%m/%Y").strftime("%Y-%m-%d")
    
    table.put_item(Item = {
                            'curp': "baz_" + response_renapo_json["curp"],
                            'apellido_paterno': response_renapo_json["paternal_surname"],
                            'apellido_materno': response_renapo_json["mothers_maiden_name"],
                            'nombre': response_renapo_json["names"],
                            'sexo': response_renapo_json["sex"], 
                            'fecha_nacimiento' : fecha_nacimiento,
                            'entidad_nacimiento': response_renapo_json["probation_document_data"]["claveEntidadRegistro"]
                            })
