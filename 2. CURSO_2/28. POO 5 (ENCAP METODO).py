# Las clases van la primera en mayuscula
class Coche():
    
    # Propiedades: Esto son estados iniciales
    # Al usar __init__ se realiza un constructor 
    # Forma para encapsular variables __ruedas
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
            chequeo = self.__chequeo_interno()            
        
        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        
        elif (self.__enmarcha and chequeo==False):
            return "Error en el chequeo. No podemos arrancar"
        
        else:
            return "El coche esta detenido"
              
    def estado(self):
        print ("El coche tiene: ", self.__ruedas ,"ruedas. Un ancho de: ", 
               self.__anchoChasis, "y un largo de ", self.__largoChasis)
     
    # Metodo encapsulado: Solo tiene accecso desde la clase y no
    # externamente
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
          
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "Cerradas"
        
        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="Cerradas"):
            return True
        else:
            return False
               
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

