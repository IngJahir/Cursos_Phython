# El nombre de las clases es en MAYUSCULA y en SINGILAR !!!
class MiPerro:
    """ Esta es un ejemplo de Clases, Objetos y Metodos con el metodo init """
    entero = 4321
    
    # El nombre de las metodos es en MINUSCULA !!!
    # Metodos: Funciones dentro una clases
    def __init__(self,raza):
        # Definicion de atributo
        self.raza = raza
    
    #ALTERNATIVA 1 PARA LADRIDO
    #def ladrido(self,ladrar):
    #    print (ladrar)

    #ALTERNATIVA 2 PARA LADRIDO
    def ladrido(self,ladrar,raza):
        print (ladrar,raza)
    
    def juego(self,jugar):
        print (juegar)
        
    def proteccion(self,proteger):
        print (proteger)
        

#ALTERNATIVA 1 PARA LADRIDO
# Instanciar un objeto de la clase
#pecas = MiPerro("DALMATA")

# Acceder al atributo
#print(pecas.raza)

# Acceder al metodo
#pecas.ladrido("Guau Guau me llamo pecas")

#ALTERNATIVA 2 PARA LADRIDO
# Informacion de sachita
sachita = MiPerro("PINCHER")     
sachita.ladrido("RRR RRR me llamo sachita",sachita.raza)

        