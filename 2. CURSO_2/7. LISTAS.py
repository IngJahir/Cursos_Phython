# Listas: Variable que permite almacenar varios y diversos tipos de datos.
# PERO PERMITE MODIFICARLOS

# Tupla con cinco items
mi_lista  = ['Maria','Pepe','Marta','Antonio',5]
mi_lista2 = ['Jose','Roberto']

# Imprimir toda la lista
print(mi_lista[:])

# Imprimir a un elemento
print(mi_lista[2])

# Los indices negativos se cuentan a partir del ultimo elemento
print(mi_lista[-1])
print(mi_lista[-2])

# Adicion de item AL FINAL DE LA LISTA mediante un metodo 
mi_lista.append('Nuevo item')
print (mi_lista)

# Adicion de item EN UN PUNTO INTERMEDIO mediante un metodo 
mi_lista.insert(2,'Nuevo item')
print (mi_lista)

# Adicion UNA LISTA mediante un metodo 
mi_lista.extend(['Sandra','Ana','Lucia'])
print (mi_lista[:])

mi_lista3 = mi_lista + mi_lista2
print (mi_lista3[:])

# Posicion de un elemento
print (mi_lista.index("Antonio"))

# Comprobar si un elemento esta en la lista
print ('Pepe' in mi_lista)

# Remover un elemento
mi_lista.remove(5)

# Remover el EL ULTIMO ELEMENTO
mi_lista.pop()

# Repetir los elementos de una lista
mi_lista4 = mi_lista * 3
print(mi_lista4)










