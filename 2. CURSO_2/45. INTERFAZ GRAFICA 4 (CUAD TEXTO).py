from tkinter import *
raiz =Tk()

# --------------------------------------
# SECCION DE CONTROL DE FRAME 
# --------------------------------------
miFrame=Frame(raiz,width=1200,height=600 )
miFrame.pack()

# --------------------------------------
# SECCION DE CONTROL DE CUADRO DE TEXTO
# --------------------------------------

# Se recomienda trabajar con el metodo grid para pocisionar los textos 
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="left")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)

# --------------------------
# SECCION DE CONTROL lABELS
# --------------------------

# Sticky alinea el texto segun los puntos cardinales
# Pad permite la sepaacion del texto entre los bordes

nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="Pasword: ")
passLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="Direccion de la casa: ")
direccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

raiz.mainloop()

