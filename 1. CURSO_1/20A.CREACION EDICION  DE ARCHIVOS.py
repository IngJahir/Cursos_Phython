from io import open

# Usar un archivo solo como lectura (r)
#file1 =open("CUADRITO1.txt","r")
#All_txt=file1.read()
#line_txt=file1.readlines()
#file1.close()
#print(line_txt[3])

# Crear un archivo y modificarlo (w)
#file2 =open("CUADRITO2.txt","w")
#    phrase = "Mi primer programita"
#    file2.write(phrase)
#file2.close()
    
# Agrear info a un archivo (a)
#file =open("CUADRITO2.txt","a")
#file.write("\nsegunda linea")
#file.close()

#Localizar el puntero
#file =open("CUADRITO2.txt","r")
#file.seek(5)
#Con read(11) se detiene la lectura en 11
#Con read() se ejecuta la lectura desde donde esta el puntero

#file.seek((len(file.read()))/2)
#file.seek(len(file.readline()))

#print(file.read())

#Leer y escribir dentro del mismo archivo
file =open("CUADRITO2.txt","r+")
file.write("Nuevo comienzo")