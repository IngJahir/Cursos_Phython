# MODULOS: Dividir programas grandes en modulos que facilita el mantenimiento 
# y lo hace mas legible

def suma():
    """ Muestra la suma de dos numeros ingresados """
    a=int(input("Ingrese el primer numero entero: "))
    b=int(input("Ingrese el segundo numero entero: "))
    print(a+b)

def resta():
    """ Muestra la resta de dos numeros ingresados """
    a=int(input("Ingrese el primer numero entero: "))
    b=int(input("Ingrese el segundo numero entero: "))
    print(a-b)  
    
def mult():
    """ Muestra la multiplicacion de dos numeros ingresados """
    a=int(input("Ingrese el primer numero entero: "))
    b=int(input("Ingrese el segundo numero entero: "))
    print(a*b)
    
def div():
    """ Muestra la division de dos numeros ingresados """
    a=int(input("Ingrese el primer numero entero: "))
    b=int(input("Ingrese el segundo numero entero: "))
    print(a/b)
    
def fib(n):
    """ Muestra la serie de fibonacci hasta el niumero n """
    x, y = 0, 1 # Asignacion multiple
    while x < n:
        print(x)
        x, y = y, x+y # x=y, y=x+y
    print ()
        
    

