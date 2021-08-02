# TUPLAS
# No permiten añadir, eliminar, mover elementos etc (no append, extend, move).
# Si permite extraer porciones, pero el resultado es una nueva Tupla.
# Si permiten comprobar si un elemento se encuentra en la tupla.

miTupla = ("Juan",13,1,1995) 
print(miTupla[2])

# Conversion de Tupla a lista
miLista = list(miTupla)
print(miLista)

# Conversion de Lista a lista
miTupla = tuple(miLista)
print(miLista)

# Comprobar si un elemento esta en la lista
print ('Juan' in miTupla)

# Contar un elemento en una tupla
print (miTupla.count(13))

# Longitud de una Tupla
print (len(miTupla))

# Tupla unitaria. USAR LA COMA AL FINAL OJO!! 
miTupla_unitaria = ("Juan",)

# Desempaquetado de tupla
nombre,dia,mes,agno = mitupla
print(nombre)
print(dia)
print(mes)|
print(agno)







