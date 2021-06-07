import json
import conexion_bmp
import conexion_dynamo
import respuesta
import validaciones


#-----------------------------------------------------------------------------------------------------------
def verificaCurp(event, context):

    print(event)
    curp =  str(event["queryStringParameters"]["curp"]).upper()
    usuario_gestor = event["queryStringParameters"]["user"]
    dominio_gestor = event["queryStringParameters"]["dominio"]

    if(validaciones.expresion_regular_curp(curp)):
        fill = conexion_bmp.verifica_registro_BMP(curp)
        if(fill==None):
            body = conexion_dynamo.get_user_dynamo(curp)
        else:
            body = validaciones.valida_estatus(fill,usuario_gestor,dominio_gestor)
    else:
        print("El curp no cumple con la expresion regular")
        body = respuesta.formato_curp_invalido()
    
    #print("El body es: ", body)
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


    