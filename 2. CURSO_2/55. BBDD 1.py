import sqlite3

miConexion=sqlite3.connect("Primera base")
miCursor=miConexion.cursor()

# ---------------------
# ENCABEZADOS REGISTRO 
# ---------------------
#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")

# -------------------------
# INGRESO DE SOLO REGISTRO
# -------------------------
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

# Confirmar cambios (commit.())
miConexion.commit()

miConexion.close()
