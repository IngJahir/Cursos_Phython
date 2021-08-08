from tkinter import*
root=Tk()

# ---------------------------
# CONFIGURACION PARA EL MENU 
# ---------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu,width=300, height=300)

# Opcion Archivo dentro del codigo 
archivoMenu=Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")
# Barra archivo enel entorno root
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)

# Opcion Edicion dentro del codigo 
archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)

# Opcion Herramientas del codigo 
archivoHerramientas=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)

# Opcion Ayuda del codigo 
archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)


root.mainloop()