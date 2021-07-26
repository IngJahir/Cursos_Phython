# POLIMORFISMO: Objetos que utilizan metodos o atributos con el mismo nombre 
# pero que tienen diferente forma de responder.
class Aeronave:
    def viajar(self):
        print("Yo viajo por los aires")

class Automovil:
    def viajar(self):
        print("Yo viajo por los caminos")

zepelin = Aeronave()
coche = Automovil()

zepelin.viajar()
coche.viajar()

