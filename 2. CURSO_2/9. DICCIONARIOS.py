miDiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"londres","Espana":"Madrid"} 
miDiccionario2 = {"Alemania":"Berlin",23:"Jordan","Mosqueteros":3}

print(miDiccionario)
print(miDiccionario["Espana"])

# Agregar elementos a un diccionario
miDiccionario["Italia"] = "Lisboa"

# Modificar el valor de la clave
miDiccionario["Italia"] = "Roma"

# Eliminar la clave y su contenido
del miDiccionario["Reino unido"]

# Utilizar las tupla para asignar las claves
miTupla('Espana','Francia','Reino Unido','Alemania')
miDiccionario3 = {mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
print(miDiccionario["Francia"])

# Diccionario dentro de un diccionario
miDiccionario4 = {23:"Jordan","Nombre":"Michel","Equipo":"Chigago","anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(miDiccionario4["anillos"])

# Claves de un Diccionario
print (miDiccionario4.keys())

# Contenido de un Diccionario
print (miDiccionario4.values())

# Longitud de un diccionario
print (len(miDiccionario4))





