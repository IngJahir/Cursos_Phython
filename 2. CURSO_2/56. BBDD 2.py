import sqlite3

miConexion=sqlite3.connect("segunda base")
miCursor=miConexion.cursor()

'''
# ---------------------
# ENCABEZADOS REGISTRO
# ---------------------

# Creacion de encabezado de los registros
miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")

# ------------------------------
# INGRESO DE MULTIPLES REGISTROS
# ------------------------------

# Lote de registros
variosProductos =[
                    ("CAMISETA", 10, "DEPORTES"),
                    ("JARRON", 10, "CERAMICAS"),
                    ("CAMION", 10, "JUGUETERIA")        
                ]
# Executemany permite la insercion de multiples registros
miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)
'''

# -----------------------
# SELECCION DE REGISTROS
# -----------------------

# Seleccion de los datos almacenados
miCursor.execute("SELECT * FROM PRODUCTOS")

# fetchall toma los registros que se seleccionaron
variosProductos=miCursor.fetchall()

for producto in variosProductos:
    print("Nombre articulo: ",producto[0]," Seccion: ",producto[2])

miConexion.commit()
miConexion.close()