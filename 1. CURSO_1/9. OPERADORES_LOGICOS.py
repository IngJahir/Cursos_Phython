# Operadores logicos: Permiten formular condiciones complejas a partir de 
# condiciones simples

# Operador AND. Recordad que [(Cond_1 = V) AND (Cond_1 = V)] = V
cond_1 = (100 == 100)
cond_2 = ('chann' == 'chann')
res = cond_1 and cond_2
print (res)
 
# Operador OR. Recordad que [(Cond_1 = F) OR (Cond_1 = F)] = F
cond_1 = (100 > 100)
cond_2 = ('chann' != 'chann')
res = cond_1 or cond_2
print (res)

# Operador OR. Invierte el resultado de la condicion 
cond_1 = (100 > 100)
res = not cond_1
print (res)

