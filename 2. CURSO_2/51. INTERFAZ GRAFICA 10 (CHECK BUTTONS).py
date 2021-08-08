from tkinter  import*

root=Tk()
root.title("Ejemplo")

# -------------------------
# DECLARACION DE VARIABLES 
# -------------------------
playa= IntVar()
montana=IntVar()
turismoRural=IntVar()

# ----------
# FUNCIONES
# ----------
def opcionesViaje():
    
    opcionEscogida=""
    if playa.get()==1:
        opcionEscogida+= "Playa "
    
    if montana.get()==1:
        opcionEscogida+= "Montaña "
    
    if turismoRural.get()==1:
        opcionEscogida+= "Turismo rural "
    
    textoFinal.config(text=opcionEscogida)

# ---------------------
# CONTROL DE LA IMAGEN
# --------------------
foto=PhotoImage(file="IMAGENES/AVION.png")
Label(root,image=foto).pack()

# ---------------------
# CONTROL DE FRAMES
# --------------------
frame=Frame(root)
frame.pack()
Label(frame, text="Elige destinos",width=50).pack()

# ---------------------
# OPCIONES CHECKBUTTON
# ---------------------
Checkbutton(root,text="playa", variable=playa, offvalue=0, onvalue=1, command=opcionesViaje).pack()
Checkbutton(root,text="Montaña",variable=montana,offvalue=0,onvalue=1, command=opcionesViaje).pack()
Checkbutton(root,text="Turismo rural",variable=turismoRural,offvalue=0,onvalue=1, command=opcionesViaje).pack()

# ---------------------
# CONTROL DE LABELS
# --------------------
textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()
