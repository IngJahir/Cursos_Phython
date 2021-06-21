# El nombre de las clases es en MAYUSCULA y en SINGILAR !!!
class MiClaseEjemeplo:
    """ Esta es un ejemplo de Clases, Objetos y Metodos """
    entero = 4321
    
    # El nombre de las metodos es en MINUSCULA !!!
    # Metodos: Funciones dentro una clases
    def mensaje (self,mensaje):
        print (mensaje)

# Instanciar un objeto de la clase
x = MiClaseEjemeplo()
y = MiClaseEjemeplo() 
    
print(x.entero)
print(x.mensaje("SALUDO !!!"))
print(y.mensaje("HOLA POO"))
   
        