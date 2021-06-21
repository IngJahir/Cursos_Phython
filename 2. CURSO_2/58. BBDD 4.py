import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

# ------------------------------
# CREACION DEL REGISTRO
# ------------------------------

# PRIMARY KEY Permite que el campo sea CLAVE,de esta forma el campo codigo no 
# podra ser repetida. 
# ID permite que la clave se genere automaticamente (linea 18). 
# UNIQUE Permite que no se repita el nombre del articulo en este caso

miCursor.execute('''
                 CREATE TABLE PRODUCTOS 
                     ( 
                     ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                     NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
                     PRECIO INTEGER, 
                     SECCION VARCHAR(20)) 
                 ''')
                     
# Lote de registros
productos =[
                    ("PELOTA", 20, "JUGUETERIA"),
                    ("PANTALON", 15, "CONFECCION"),
                    ("DESTORNILLADOR", 25, "FERRETERIA"),
                    ("JARRON", 45, "CERAMICA"),
                    ("JARRONES 123", 45, "CERAMICA")
                ]

# Executemany permite la insercion de multiples registros
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)

miConexion.commit()
miConexion.close()