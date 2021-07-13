# Tupla: Variable que permite almacenar varios y diversos tipos de datos
# inmutables.

# Tupla con cuatro items
mi_tupla = ('Indice cero', 2 , 3.0 , 'indice tres') 

# Impresion con indices positivos
print (mi_tupla[0])
print (mi_tupla[1])
print (mi_tupla[2])
print (mi_tupla[3])

# Impresion con indices negativos
print (mi_tupla[-1])
print (mi_tupla[-2])
print (mi_tupla[-3])
print (mi_tupla[-4])

# Seccion de la Tupla.
# El ultimo indice no es considerado, en esta caso va de 1 a 3 

# Selecction desde el primer dato
print (mi_tupla[:3])

# Selecction desde 1 hasta 2
print (mi_tupla[1:3])

# Selecction desde 1 hasta el ultimo dato
print (mi_tupla[1:])
