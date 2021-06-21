class Ejemplo:
    def __init__(self):
        self.__oculto = "Me encuentro oculto en la clase"
    
    def publico(self):
        return "Soy un metodo publico. A la vista de todos"
    
    # El metodo privado usa dos underline antes del metodo __metodo
    def __privado(self):
        print ("Dentro de la clase me pueden ver")
    
    def get_oculto(self):
        return self.__oculto
    
    def set_oculto(self):
        self.__oculto = self.__privado()
    
# Instancia de objetos
objeto = Ejemplo()

#print(objeto.publico())
#print(objeto.__privado())    

# Para ver el encapsulamiento hay que uasr los underline
# Objeto._Clase__Metodo()
#print(objeto._Ejemplo__privado())        
      
print(objeto.get_oculto())
objeto.set_oculto()

