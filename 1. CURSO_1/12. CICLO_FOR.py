# Bucle FOR: Permite realizar iteraciones sobre una variable compleja ya sea 
# por lista o tupla

#Por cada lenguaje en mi lista
mi_lista=["Python","Java","C++","PHP","Ruby"]
for lenguaje in mi_lista:
    print (lenguaje)

#Imprimir edades desde 10 hasta 17 
for edad in range(10,18):
    print ("Tu edad es: ",edad)
    
#Tabla de multiplicar
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplicar = int (input("Que tabla de multiplicar desea?:  "))
for numero in tabla:
    print (multiplicar," X ",numero," = ", multiplicar*numero)

#Elementos de un arreglo
for i in range(0,5):
    for j in range(0,5):
        print("M[",i,",",j,"] =",(2*i)+j)
    
    

    
    




