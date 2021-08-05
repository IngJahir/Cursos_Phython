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

raiz.mainloop()
