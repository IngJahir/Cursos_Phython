from tkinter import *

# --------------------
# lISTADO DE FUNCIONES 
# --------------------

def imprimir(texto): 
    print (texto)
    
v0=Tk()
'''
# -----------------------------
# CONFIGURACION PARA LA IMAGEN
# -----------------------------
imagen1=PhotoImage(file="ROCKET.png")
label1 = Label(v0, image=imagen1) 
label1.grid(row=1,column=1)
'''
# ---------------------------
# CONFIGURACION PARA EL MENU
# ---------------------------

menu1 = Menu(v0)
v0.config(menu=menu1)
# Opcion AMARILLO dentro del codigo 
menu1.add_cascade(label="AMARILLO", menu=menu1_1)
menu1_1 = Menu(menu1, tearoff=0)
menu1_1.add_cascade(label="FRUTAS", menu=menu1_1_1)
menu1_1_1 = Menu(menu1_1, tearoff=0)
menu1_1_1.add_command(label="BANANO",command=lambda: imprimir("BANANO"))
menu1_1_1.add_command(label="PIÑA",command=lambda: imprimir("PIÑA"))

# Opcion ROJO dentro del codigo 
menu1.add_cascade(label="ROJO", menu=menu1_2)
menu1_2 = Menu(menu1, tearoff=0)
menu1_2.add_command(label="SANGRE",command=lambda: imprimir("SANGRE"))
menu1_2.add_separator()
menu1_2_1 = Menu(menu1_2, tearoff=0)
menu1_2.add_cascade(label="FRUTAS", menu=menu1_2_1)
menu1_2_1.add_command(label="FRESA",command=lambda: imprimir("FRESA"))
menu1_2_1.add_command(label="MANZANA",command=lambda:imprimir("MANZANA"))


v0.mainloop()
