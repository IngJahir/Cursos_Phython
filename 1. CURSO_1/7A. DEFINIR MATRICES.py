
nro_points=3
fi_point=3

# Definición de matrices        
fi_point = nro_points
co_point = 3
matrix_point=[]

for i in range(fi_point):
    matrix_point.append([0]*co_point)
    
# Llenado de matrices
print("MATRIX POINTS \n")
for i in range (0,(nro_points)):
    for j in range (0,3):
        matrix_point[i][j]=i*j
    print()

# Impresion de matrices
print("MATRIX POINTS \n")
for i in range (0,(nro_points)):
    for j in range (0,3):
        print(matrix_point[i][j]," ",end="")
    print()