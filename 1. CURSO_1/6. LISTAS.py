# Listas: Variable que permite almacenar varios y diversos tipos de datos
# PERO PERMITE MODIFICARLOS

# Tupla con cinco items
mi_lista = ['Indice cero', 24 , 13.14 , True , [1,2]]

# Impresion con indices positivos
print (mi_lista[0])
print (mi_lista[1])
print (mi_lista[2])
print (mi_lista[3])
print (mi_lista[4])

# Impresion con indices negativos
print (mi_lista[-1])
print (mi_lista[-2])
print (mi_lista[-3])
print (mi_lista[-4])
print (mi_lista[-5])

# Seccion de la Lista
# El ultimo indice no es considerado, en esta caso va de 1 a 3 

# Selecction desde el inicio hasta segundo dato
print (mi_lista[:3])

# Selecction desde 1 hasta 2
print (mi_lista[1:3])

# Selecction desde 1 hasta el ultimo dato
print (mi_lista[1:])

#Cambio de un solo dato
mi_lista[1]=False
print (mi_lista)

#Cambio de varios datos
mi_lista[1:4] = [8 , 9 , 10]
print (mi_lista)

#Adicion de item mediante un metodo
mi_lista.append('Nuevo item')
print (mi_lista)

#Tamaño de la lista
Dim = len(mi_lista)
print (Dim)


