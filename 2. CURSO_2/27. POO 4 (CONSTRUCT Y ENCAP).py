# Las clases van la primera en mayuscula
class Coche():
    
    # Propiedades: Esto son estados iniciales
    # Al usar __init__ se realiza un constructor 
    # Forma para encapsular variables __ruedas
    # Encapsuar un atributo es protegerlo para que no lo modifiquen desde afuera
    # pero si es modificable dentro de la clase
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
    
    # Los Metodos correspornden a los comportamientos 
    # Los Metodos son funciones que pertenecen a la clase
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        
        if (self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta detenido"
              
    def estado(self):
        print ("El coche tiene: ", self.__ruedas ,"ruedas. Un ancho de: ", 
               self.__anchoChasis, "y un largo de ", self.__largoChasis)
        
          
# Objeto 1
# Para instanciar una clase se ponen los ()
miCoche = Coche()
print("Coche 1")
print(miCoche.arrancar(True))
miCoche.estado()


# Objeto 2
# Para instanciar una clase se ponen los ()
miCoche2 = Coche()
print("Coche 2")
print(miCoche2.arrancar(False))
miCoche2.ruedas=2
miCoche2.estado()

