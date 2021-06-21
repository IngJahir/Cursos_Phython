# ------------
# SUPER CLASE
# ------------
class Vehiculos():
    
    def __init__ (self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar (self):
        self.enmarcha=True
        
    def acelerar(self):
        self.acelera=True
        
    def frenar(self):
        self.frena=True
                
    def estado(self):
        print("Marca ",self.marca,"\nModelo: ",self.modelo,
              "\nEn marcha: ",self.enmarcha,"\nAcelera: ",self.acelera,
              "\nFrena: ",self.frena)

# ------------------------
# HERENCIA DE JERARQUIA 1
# ------------------------
# Esta clase hereda la informacion de vehiculos  

class Furgoneta(Vehiculos):
    
    def carga(self,cargar):
        
        self.cargado=cargar
        
        if(self.cargado==cargar):
            print("La furgoneta esta cargada")
        else:
            print("La furgoneta no esta cargada")
          
class Moto(Vehiculos):
    
    hcaballito=" "
    
    def caballito(self):
        self.hcaballito = "Voy a hacer el caballito"
    
    # Se crea una copia del metdodo estado proveniente de la clase vehiculos
    # y esta pasa a tener la prioridad, esto se conoce como sobreescribir un
    # metodo
    def estado(self):
        print("Marca ",self.marca,"\nModelo: ",self.modelo,
              "\nEn marcha: ",self.enmarcha,"\nAcelera: ",self.acelera,
              "\nFrena: ",self.frena,"\n",self.hcaballito )
        

# --------------------------------------
# HERENCIA DE JERARQUIA 1 CASO MULTIPLE
# --------------------------------------
# Herencia multiple
class BicicletaElectrica(VElectricos,Vehiculos):
    pass

# ---------------------
# METODO INDEPENDIENTE
# ---------------------
# La funcion super ejecuta las clases de la clase padre
class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        
        super().__init__(marca, modelo)
        
        self.autonomia=100
        
    def cargarEnergia(self):
        self.cargando = True
        
    def estado(self):        
        super().estado()

print("INFORMACION MOTO")
miMoto=Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

print("INFORMACION FURGONETA")
miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)

print("INFORMACION BICICLETA")
miBici=BicicletaElectrica("Benoto","xt125")
miBici.estado()

