from tkinter import*
from tkinter import messagebox
import sqlite3

# ---------------------
# LISTADO DE FUNCIONES
# ---------------------

root = Tk()


miFrame2=Frame(root)
miFrame2.pack()

# Boton DELATE
botonBorrar=Button(miFrame2,text="VENTANA")
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10,comand=click)


root.mainloop()