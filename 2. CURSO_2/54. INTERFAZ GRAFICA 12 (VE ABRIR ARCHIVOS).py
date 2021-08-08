from tkinter import * 
from tkinter import filedialog

root = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(initialdir = "/",title = "Abrir",filetypes = (("Ficheros de Excel","*.xlsx"),("Ficheros de Texto","*.txt"),("Todos los ficheros","*.*")))
    print (fichero)
    
Button(root,text="Abrir fichero",command=abreFichero).pack()

root.mainloop()