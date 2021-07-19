# *********************************
# ******* SUPER CLASE STARK *******
# ********************************* 
# SUPER-CLASE: Esta clase corresponde a los padre
class CasaStark: 
    """ Personajes de Games of Thrones Casa Stark """
    
    print ("Hijos de Eddard Stark y Lady Catelin")
    def __init__(self,apellido_stark):
        self.apellido_stark = apellido_stark
        
# SUB-CLASE: Esta clase corresponde a los hijos
class HerederoStark(CasaStark):
    """ Sub-clase que hereda de la clase CasaStark"""
    
    def nombre(self,nombre,apellido_stark):
        print("Mi nombre es", nombre , "Heredero de la casa ", apellido_stark)
       
# Instancia de objetos        
robb = HerederoStark("Stark")
sansa = HerederoStark("Stark")
arya = HerederoStark("Stark")
bran = HerederoStark("Stark")
rick = HerederoStark("Stark")

# Acceso a metodos y atributos (objeto.metodo)
print (robb.nombre("Robb",robb.apellido_stark))
print (sansa.nombre("Sansa",sansa.apellido_stark))
print (arya.nombre("Arya",arya.apellido_stark))        
print (bran.nombre("Bran",bran.apellido_stark))    
print (rick.nombre("Rick",rick.apellido_stark)) 

# *************************************
# ******* SUPER CLASE TARGARYEN *******
# *************************************
        
# SUPER-CLASE: Esta clase corresponde a los padre
class CasaTargaryen:
    """ Personajes de Games of Thrones Casa Targaryen """
    
    print ("Hijos de Aerys - El rey loco")
    def __init__(self,apellido_targaryen):
        self.apellido_targaryen = apellido_targaryen
        
# SUB-CLASE: Esta clase corresponde a los hijos
class HerederoTargaryen(CasaTargaryen):
    """ Sub-clase que hereda de la clase Casa Targaryen"""
    
    def nombre_t(self,nombre_t,apellido_targaryen):
        print("Mi nombre es", nombre_t , "Heredero de la casa ", apellido_targaryen)

# Instancia de objetos
daenerys = HerederoTargaryen("Targaryen")
vicerys = HerederoTargaryen("Targaryen")

# Acceso a metodos y atributos (objeto.metodo)
print (daenerys.nombre_t("Daenerys",daenerys.apellido_targaryen))
print (vicerys.nombre_t("Vicerys",daenerys.apellido_targaryen))







    
