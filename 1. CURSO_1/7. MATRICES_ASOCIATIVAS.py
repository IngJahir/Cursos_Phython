# Diccionario: Permiten utilizar una clave para declarar y acceder a un valor.
# La clave puede ser cualquier valor INMUTABLE

# La clave del diccionario es con CORCHETES 
mi_diccionario = {'clave_1':'valor_1' , 'clave_2':2 , 'clave_3':3.33}
print (mi_diccionario['clave_2'])

# Modificacion de una clave del diccionario
mi_diccionario['clave_3']='NUEVO VALOR'
print (mi_diccionario['clave_3'])

# Eliminar elemento del diccionario
del(mi_diccionario['clave_1'])
print (mi_diccionario)

# Diccionario con tupla al final
mi_diccionario_2 = {'clave_1':'valor_1' , 'clave_2':2 , 'clave_3':3.33 , (1,2):[5,6,7]}
print (mi_diccionario_2 [(1,2)])


