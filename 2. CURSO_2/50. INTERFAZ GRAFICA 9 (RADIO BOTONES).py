from tkinter import*
root = Tk()
varOpcion= IntVar()

# --------------------------
# FUNCIONES DE LAS OPCIONES 
# -------------------------

def imprimir ():
    
    #print(varOpcion.get())
    
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido Masculino")
        
    elif varOpcion.get()==2:
        etiqueta.config(text="Has elegido Femenino")
    
    else:
        etiqueta.config(text="Has elegido otras opciones")

# ---------------------
# LABEL DE INFORMACION
# ---------------------
Label(root,text="Genero:").pack()
 
# ------------------------------------
# SECCION DE CONTROL DEL RADIO BUTTON
# -----------------------------------
Radiobutton(root,text="Masculino",variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(root,text="Femenino",variable=varOpcion, value=2,command=imprimir).pack()

Radiobutton(root,text="Otras opciones",variable=varOpcion, value=3,command=imprimir).pack()

# -------------------
# ETIQUETA DE SALIDA
# -------------------

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()

