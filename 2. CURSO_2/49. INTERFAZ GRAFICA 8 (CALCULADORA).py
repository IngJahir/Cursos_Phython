from tkinter import *
raiz = Tk()
raiz.resizable(False,False)
# -----------------------------
# SECCION DE CONTROL DEL FRAME
# -----------------------------
miFrame=Frame(raiz)
miFrame.pack()

# --------------
# DECLARRACIONES
# --------------
numeroPantalla=StringVar()
operacion=""
resultado = 0


# ---------
# PANTILLA
# ---------
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10,columnspan=4)
pantalla.config(background ="black",fg="#03f943", justify="right")
                
# -----------------------
# FUNCIONES DE PULSACION
# -----------------------
def numeroPulsado (num):
    global operacion
    
    if operacion!="":
        numeroPantalla.set(num)
        operacion=""        
    else:
        numeroPantalla.set(numeroPantalla.get() + num) 

def suma(num):
    global operacion
    global resultado
    
    resultado+=int (num) #resultado = resultado + int(num)    
    operacion = "suma"    
    numeroPantalla.set(resultado) 
    
def el_resultado ():
    global resultado
    
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado = 0
    
                    
# ----------------
# TECLADO NUMERICO
# ----------------
# lambdda: Es una funcion anonima la cual permite que la funcion numeroPulsado 
# se active unicamente al oprimir el boton respectivo.

# FILA 5
boton0 = Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)

# FILA 4
boton1 = Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)

boton2 = Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)

boton3 = Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)

# FILA 3
boton4 = Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)

boton5 = Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)

boton6 = Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)

# FILA 2
boton7 = Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)

boton8 = Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)

boton9 = Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)

# -----------------------------
# TECLA DE OPERACIONES BASICAS
# -----------------------------
# FILA 5
botonSum = Button(miFrame,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)            
# FILA 4
botonRest = Button(miFrame,text="-",width=3)
botonRest.grid(row=4, column=4)            
# FILA 3
botonMult = Button(miFrame,text="X",width=3)
botonMult.grid(row=3, column=4)            

# FILA 2
botonDivi = Button(miFrame,text="/",width=3)
botonDivi.grid(row=2, column=4)            

# FILA 5
botonDeci = Button(miFrame,text=",",width=3,command=lambda:numeroPulsado(","))
botonDeci.grid(row=5, column=2)            

botonIgua = Button(miFrame,text="=",width=3,command=lambda:el_resultado())
botonIgua.grid(row=5, column=3)            

raiz.mainloop()