from tkinter import*
from tkinter import messagebox
import sqlite3

# ---------------------
# LISTADO DE FUNCIONES
# ---------------------

def conexionBBDD():
    
    miConexion=sqlite3.connect("Usuarios")    
    miCursor=miConexion.cursor()
    
    try: 
        miCursor.execute("CREATE TABLE DATOS_USARIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE_USUARIO VARCHAR(50),PASSWORD VARCHAR(50), APELLIDO VARCHAR(10),DIRECCION VARCHAR(50),COMENTARIOS VARCHAR(100) )")
        messagebox.showinfo("BBDD","BBDD creada con exito")
    except:
        messagebox.showwarning("ATENCION!!","La BBDD ya existe")
        
def salirAplicacion():
    valor=messagebox.askquestion("SALIR", "¿Desea salir de la aplicacion?")
    
    if valor=="yes":
        root.destroy()
        
def limpiarCampos():
    miID.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    textoComentario.delete("1.0",END)
       
def crear():
    miConexion=sqlite3.connect("Usuarios")    
    miCursor=miConexion.cursor()
           
    """
    # Metodo largo
    miCursor.execute("INSERT INTO DATOS_USARIOS VALUES(NULL,'" + miNombre.get() + 
       "','" + miPass.get() + 
       "','" + miApellido.get() + 
       "','" + miDireccion.get() + 
       "','" + textoComentario.get("1.0",END) + "')")
    """
    
    # Metodo corto
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0",END)
    miCursor.execute("INSERT INTO DATOS_USARIOS VALUES(NULL,?,?,?,?,?)",(datos))
        
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito!!")
    
def leer():
    miConexion=sqlite3.connect("Usuarios")    
    miCursor=miConexion.cursor()
    
    miCursor.execute("SELECT * FROM DATOS_USARIOS WHERE ID=" + miID.get())
    elUsuario=miCursor.fetchall()
    for usuario in elUsuario:
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentario.insert("1.0",usuario[5])
        
    miConexion.commit()
      
def actualizar():
    miConexion=sqlite3.connect("Usuarios")    
    miCursor=miConexion.cursor()
    
    """
    # Metodo largo
    miCursor.execute("UPDATE DATOS_USARIOS SET NOMBRE_USUARIO='" + miNombre.get()+
                     "',PASSWORD='" + miPass.get() +
                     "',APELLIDO='" + miApellido.get() +
                     "',DIRECCION='" + miDireccion.get() +
                     "',COMENTARIOS='" + textoComentario.get("1.0",END) + 
                     "'WHERE ID=" + miID.get())
    """
    # Metodo corto
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0",END)
    miCursor.execute("UPDATE DATOS_USARIOS SET NOMBRE_USUARIO=?, PASSWORD=?,APELLIDO=?,DIRECCION=?, COMENTARIOS=? "+
                     "WHERE ID=" + miID.get(),(datos))

                                                       
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro actualizado con exito!!")

def eliminar():
    
    miConexion=sqlite3.connect("Usuarios")    
    miCursor=miConexion.cursor()
    
    miCursor.execute("DELETE FROM DATOS_USARIOS WHERE ID=" + miID.get())
       
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro eliminado con exito!!")

    
    
root = Tk()

# ---------------------------
# CONFIGURACION PARA EL MENU
# ---------------------------
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300 )

# Opcion para BBDD
bbddMenu = Menu(barraMenu,tearoff=0)
bbddMenu.add_command(label="Conectar",command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)

# Opcion para BORRAR
bbddBorar = Menu(barraMenu,tearoff=0)
bbddBorar.add_command(label="Borrar campos", command=limpiarCampos)
barraMenu.add_cascade(label="BORRAR",menu=bbddBorar)

# Opcion para CRUD
crudMenu=Menu(barraMenu,tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)

# Opcion para AYUDA
ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")
barraMenu.add_cascade(label="AYUDA",menu=ayudaMenu)

# ---------------------------
# FRAME 1: DATOS DE INGRESO
# ---------------------------

miFrame=Frame(root)
miFrame.pack()

# Cada seccion esta compuesta por un label y un cuadro de entrada

# Informacion ID
miID=StringVar()
idLabel=Label(miFrame, text="ID:")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)
cuadroID=Entry(miFrame,textvariable=miID)
cuadroID.grid(row=0,column=1,padx=10,pady=10)

# Informacion NOMBRE
miNombre=StringVar()
nombreLabel=Label(miFrame, text="NOMBRE:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)
cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)
cuadroNombre.config(fg="red",justify="right")

# Informacion PASSWORD
miPass=StringVar()
passLabel=Label(miFrame, text="PASSWORD:")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)
cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show="?")

# Informacion APELLIDO
miApellido=StringVar()
apellidoLabel=Label(miFrame, text="APELLIDO:")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)
cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10)

# Informacion DIRECCION
miDireccion=StringVar()
direccionLabel=Label(miFrame, text="DIRECCION:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)
cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

# Informacion COMENTARIO
texoLabel=Label(miFrame, text="COMENTARIO:")
texoLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)
textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10)
# Barra de visualizacion
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

# ---------------------------
# FRAME 1: BOTONES INFERIORES
# ---------------------------

miFrame2=Frame(root)
miFrame2.pack()

# Boton CREATE
botonCrear=Button(miFrame2,text="CREATE",command=crear)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

# Boton READ
botonLeer=Button(miFrame2,text="READ",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

# Boton UPDATE
botonActualizar=Button(miFrame2,text="UPDATE",command=actualizar)
botonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

# Boton DELATE
botonBorrar=Button(miFrame2,text="DELATE",command=eliminar)
botonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)

root.mainloop()

