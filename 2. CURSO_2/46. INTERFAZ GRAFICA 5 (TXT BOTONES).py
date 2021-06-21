from tkinter import *

# ---------------------
# lISTADO DE FUNCIONES
# ---------------------
def CodigoBoton ():
    minombre.set("Juanito Alimaña")

# --------------------------------------
# SECCION DE CONTROL DE FRAME
# --------------------------------------
    
raiz =Tk()
miFrame=Frame(raiz,width=1200,height=600 )
miFrame.pack()

# Esta definicion  de variable debe hacerse dentro del frame que utiliza las 
# variables
minombre=StringVar()

# --------------------------------------
# SECCION DE CONTROL DE CUADRO DE TEXTO
# --------------------------------------

# Se recomienda trabajar con el metodo grid para pocisionar los textos 
cuadroNombre=Entry(miFrame, textvariable=minombre)
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

direccionLabel=Label(miFrame,text="Direccion: ")
direccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

comentariosLabel=Label(miFrame,text="Comentarios: ")
comentariosLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

# ----------------------------
# SECCION DE CUADROS DE TEXTO
# ----------------------------
textoComentario=Text(miFrame,width=16,height=10)
textoComentario.grid(row=4,column=1,padx=10,pady=10)

# ----------------------------------
# SECCION DE BARRA DE DESPLAZAMIENTO
# ----------------------------------
# Sticky en este caso adapta el tamaño de la barra de desplazamiento
# En este caso textoComentario.config debe pocisonarse en este punto para que
# el cursor coincida con la linea de texto
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

# -------------------
# SECCION DE BOTONES
# -------------------
botonEnvio=Button(raiz,text="Enviar",command=CodigoBoton)
botonEnvio.pack()

raiz.mainloop()

