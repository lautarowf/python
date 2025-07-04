notas_validas = 0
notas_invalidas = 0
nota = 0
suma_notas = 0
while nota != -1:
  nota = int(input("Ingrese una nota o -1 para salir"))
  if nota >=1 and nota <=10:
    notas_validas += 1
    suma_notas += nota
  elif nota == -1:
    break
  else:
    notas_invalidas +=1
if notas_validas > 0:
    print("Promedio notas: ", suma_notas/notas_validas)
else:
    print("No se ingresaron notas validas")
print("Notas fuera de rango: ", notas_invalidas)