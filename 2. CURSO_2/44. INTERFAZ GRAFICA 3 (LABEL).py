from tkinter import *
root = Tk()

miFrame =Frame(root,width=500,height=400) 
miFrame.pack()

miImagen=PhotoImage(file="IMAGENES/ROCKET.png")

# ----------------------------
# SECCION DE CONTROL DE LABEL
# ----------------------------

# Opcion 1 para label
# miLabel=Label(miFrame,text ="hola alumnos de python")
# miLabel.place(x=100,y=200)

# Opcion 2 para label
# Label(miFrame,text ="hola alumnos de python",fg="red",font=("Times new roman",18)).place(x=100,y=200)

# Opcion 3 para introduccion de imagen
Label(miFrame,image = miImagen).place(x=100,y=200)

root.mainloop()

