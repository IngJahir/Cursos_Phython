cadena = input("Digite una cadena de texto: ")

# Obtiene la longitud de una cadena.
print("\nEl numero de caracteres de la cadena es: ", len(cadena))

# Devuelve verdadero si la cadena contiene solo letras.
if cadena.isalpha():
    print("\nLa cadena es alfabetica")
    
# Devuelve verdadero si la cadena contiene solo numeros.
if cadena.isdigit():
    print("\nLa cadena es numerica")
    
# Convierte cadena a mayusculas. 
print ("\nEn mayuscula: ", cadena.upper())

# Convierte cadena a minuscula.
print ("\nEn miniscula: ", cadena.lower())

# Convierte mayuscula a minuscula y viceversa.
print ("\nEn mayuscula: ", cadena.swapcase())

#Reemplaza.
print("Reemplaza a por x: ", cadena.replace ("a","x"))

# Devuelve la posicion de caracter solicitado (La primera instancia).
print("\nLa posicion del caracter solicitado es: ", cadena.find("a"))

# Devuelve la posicion de caracter solicitado (La ultima instancia).
print("\nLa posicion del caracter solicitado es: ", cadena.rfind("a"))

# Crear una lista de sub-cadenas de la cadena.
z=cadena.split("a")
print("Lista de sub-cadenas: ", cadena.split("a"))
print(z[0])
print(z[1])
print(z[2])
print(z[3])
