# SUPER-CLASE: Abuelo
class Abuelo: 
    def __init__(self,temperamento):
        self.temperamento = temperamento

# SUPER-CLASE: Padre
class Padre:
    
    # Caso 2: Activar este metodo y dar la prioridad al padre 
    def __init__(self,hoby):
        self.hoby = hoby
        
    def oficio(self):
        return "Programador"
    
# SUB-CLASE: Hijo
# Caso 1: En este caso el Abuelo es prioritario y se ejecuta el init del Abuelo
#class Hijo(Abuelo,Padre):

# Caso 2: En este caso el Padre es prioritario y se ejecuta el init del padre
class Hijo(Padre,Abuelo):
   
    # Se usa cuando no se requiere ejecutar ninguna accion
    pass 
        
# Caso 1
# Instancia de objetos 
#carlos = Hijo("ALEGRE")
# Accedemos al metodo oficio() de la clase Padre
# y al metodo __init__ de la clase Abuelo e imprimimos resultados
#print("Por mi padre soy ",carlos.oficio(), "y por mi abuelo soy de caracter", 
#      carlos.temperamento)

# Caso 2
# Instancia de objetos 
carlos = Hijo("La lectura")
# Accedemos al metodo __init__ de la clase padre
# y al metodo oficio del padre
print("Por mi padre me gusta ",carlos.hoby, "\n y trabajo como", carlos.oficio())
