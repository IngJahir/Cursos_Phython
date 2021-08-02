# Las clases van la primera en mayuscula.
class Coche():
    
    # Propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    # Los Metodos correspornden a los comportamientos 
    # Los Metodos son funciones que pertenecen a la clase
    def arrancar(self):
		# Al llamar arrancar self se convierte 
		# en miCoche.enmarcha = True
        self.enmarcha = True
        
    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta detenido"
    
# Objetos
# Para instanciar una clase se ponen los ()
miCoche = Coche()
print("El largo del coche es: ",miCoche.anchoChasis)
print("El coche tiene: ",miCoche.ruedas ,"ruedas")

#Llamar el metodo
miCoche.arrancar()
print(miCoche.estado())



