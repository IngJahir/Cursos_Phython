from tkinter import * # Importa el módulo 

# --------------------
# lISTADO DE FUNCIONES
# --------------------
def mostrar(ventana): 
    ventana.deiconify() 
    
def ocultar(ventana):
    ventana.withdraw() 
    
def ejecutar(f): 
    v0.after(200,f)

def imprimir (texto):
    print (texto)
    

# -----------------
# VENTANA PRINCIPAL
# -----------------
# Tk() Es la ventana principal
v0 = Tk()
v0.config(bg="black") 
v0.geometry("500x500") 

# -------------------
# LISTADO DE BOTONES
# -------------------
# Primer botón
#b1=Button(v0,text="ABRIR VENTANA V1",command=lambda:ejecutar(mostrar(v1)))  
#b1=Button(v0,text="ABRIR VENTANA V1",command=lambda:ejecutar(mostrar(v1)) or imprimir("hola")) # Primer botón
b1=Button(v0,text="ABRIR VENTANA V1",command=lambda:ejecutar(mostrar(v1)) or imprimir("hola") or imprimir("tercera función"))
b1.grid(row=1,column=1) # El botón es cargado 

# Segundo botón 
b2=Button(v0,text="OCULTAR VENTANA V1",command=lambda:ejecutar(ocultar(v1))) 
b2.grid(row=1,column=2) # El botón es cargado

# Tercer boton
b3=Button(v0,text="SALIR",command=lambda: ejecutar(ocultar(v1)))
b3.grid(row=1,column=3) # El botón es cargado

# -------------
# VENTANA HIJA
# -------------
v1=Toplevel(v0)

# Elimina la opción de salir para evitar el error
v1.protocol("WM_DELETE_WINDOW", "onexit") 

# oculta v1 
v1.withdraw() 

# Es el evento que llama al inicio de nuestro programa.Siempre lo lleva la ventana principal.
v0.mainloop() 