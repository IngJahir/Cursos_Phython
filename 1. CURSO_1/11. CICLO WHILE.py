# Estructura de control iterativa: Permite ejecutar un bloque de codigo hasta 
# que la condicion deje de cumplirse o un numero determinado de veces 

Respuesta = "si"
numero = 0
while Respuesta == 'si':
    numero = int(input("Digite un numero: "))
    if numero > 0:
        print("El numero ingresado es positivo")
    elif numero <0:
        print("El numero ingresado es negativo")
    else:
        print("El numero ingresado es cero")
    Respuesta = input("Quieres ingresar otro numero? <si-no>")
        
    

