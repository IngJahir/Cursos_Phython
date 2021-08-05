from tkinter import *

raiz =Tk()
# ------------------------------
# SECCION DE CONTROL DE LA RAIZ 
# ------------------------------
 
# Titulo de la raiz
raiz.title("ventana de pruebas")

# Cambio de tamaño con el mouse
raiz.resizable(True,True)

# Definicion de tamaño de la raiz
raiz.geometry("650x350")

# Agregar icono a la raiz
raiz.iconbitmap("ICONOS/Icono.ico")

# Color en el fondo de la raiz 
raiz.config(bg="blue")

# -----------------------------
# SECCION DE CONTROL DEL FRAME
# -----------------------------

# Definicion de Frame
miFrame=Frame()

# Colocar frame en una raiz
miFrame.pack()

# Localizacion frame n (Norte)
# miFrame.pack(side="left",anchor="n")

# expancion del frame en y
# miFrame.pack(fill="x",expand=True)

# Color en el fondo del frame
miFrame.config(bg="red")

# Dimension del frame
miFrame.config(width="150",height="150")

# Tamaño y definicion del borde
miFrame.config(bd=35)
miFrame.config(relief="sunken")

miFrame.config(cursor="pirate")

raiz.mainloop()
