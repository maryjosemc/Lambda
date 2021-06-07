
import mysql.connector
import settings

DB_HOST = settings.DB_HOST
DB_USER = settings.DB_USER   
DB_SCHEMA =  settings.DB_SCHEMA
DB_PASSWORD = settings.DB_PASSWORD

#-----------------------------------------------------------------------------------------------------------
mydb = mysql.connector.connect(
                        host = DB_HOST, 
                        user = DB_USER, 
                        passwd = DB_PASSWORD, 
                        database = DB_SCHEMA)
conexion= mydb.cursor(dictionary=True)


#-----------------------------------------------------------------------------------------------------------      
seleccion = "domain, user, value003"
for i in range(4,12):
        if i<10:
                seleccion = seleccion + ", " + "value00" + str(i)
        else:
                seleccion = seleccion + ", " + "value0" + str(i)


#-----------------------------------------------------------------------------------------------------------

def verifica_registro_BMP(curp):
    fill=None
    query = "select " + seleccion + "  from fills where source_id=(SELECT max(source_id) from fills where ident2='" + curp + "' and template_id in (21672,21673) and last=1)"
    print("Query: " , query)
    conexion.execute(query)
    for fill in conexion:
        print(fill)
        return fill
    return fill

#-----------------------------------------------------------------------------------------------------------

def nombre_dominio(domain):
    fill=None
    query = "select name from domains where id = " + str(domain)
    conexion.execute(query)
    for fill in conexion:
        print(fill)
        return fill["name"]
    return fill