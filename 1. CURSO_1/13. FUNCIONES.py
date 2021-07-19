# FUNCIONES: Bloque de codigo con un nombre asignado que tiene como objetivo 
# realizar tares especificas y devolver un resultado. 

def mi_funcion1():
    """ Funcion 1 : Imprime mensaje de saludo """
    print("Hola a todos")
    print("Esta es mi primera funcion")
    
def mi_funcion2(cadena,numero):
    """ Funcion 2 : Escribe una cadena de texto el numero de veces que le 
    asignamos un numero """
    print(cadena * numero)

def mi_funcion3(cadena,numero=4):
    """ Funcion 3 : Escribe una cadena de texto por default 4 veces """
    print(cadena * numero)
    
def Cuadrado1(num):
    """ Cuadrado 1 : Muestra el cuadrado de un numero """
    print(num * num)
    
def Cuadrado2():
    """ Cuadrado 2 : Imprime el cuadrado de un numero ingresado """
    n = int(input("Ingrese un numero: "))
    Cuadrado1(n)

def Cuadrado_return():
    """ Cuadrado_return : Retorna el cuadrado de un numero """
    n = int(input("Ingrese un numero: "))
    return n*n
    
    
    
    


