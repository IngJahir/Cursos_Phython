class Coche(): 
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
    
    def color(self):
        print("Negro")
        
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
    
    def color(self):
        print("Gris")
    
class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")
    
    def color(self):
        print("Verde")

# ------------------
# SIN POLIMORFISMO
# ------------------
"""
miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2=Coche()
miVehiculo2.desplazamiento()

miVehiculo3=Camion()
miVehiculo3.desplazamiento()
""" 
# -------------------------
# POLIMORFISMO CON FUNCION
# -------------------------
def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Moto()
desplazamientovehiculo(miVehiculo)

# ------------------------
# POLIMORFISMO CON METODO
# ------------------------
Mazda    = Coche()
Susuky   = Moto()
Kenworkt = Camion()
for vehiculo in (Mazda,Susuky,Kenworkt):
    vehiculo.color()

# -------------------------
# POLIMORFISMO CON HERENCIA
# -------------------------


