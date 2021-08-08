from tkinter import*
from tkinter import messagebox

root=Tk()


# ---------------------------
# FUNCIONES VENTANA EMERGENTE 
# ---------------------------
def infoAdicional():
    messagebox.showinfo("Procesador de Juan","Procesador de textos version 2018")

def avisoLicencia ():
    messagebox.showwarning("Licencia","Producto baja licencia GNU")
    
def salirAplicacion():
    '''
    valor= messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")    
    if valor == "yes":
        root.destroy()
    '''       
    valor= messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
    if valor == "True":
        root.destroy()
        
def cerrarDocumento():
    valor= messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
    if valor==False:
        root.destroy()
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
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)
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
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional )

barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)


root.mainloop()