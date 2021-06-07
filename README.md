# Lambda verificaCurp

Esta lambda esta encarga de verificar que el curp del ususario que se desea registrar sea unico

Se verifica que el CURP:

-Cumpla con la estructura de un curo con base en una expresion regular
-Exista en la base de datos bmc en alguno de los dominios correspondientes a baz
-Sea valido en RENAPO
-Ya exista en la tabla curps_unicos (Si existe regresa la informacion acorde al curp y si no, consulta en RENAPO)
