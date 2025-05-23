#calcular el dia siguiente
print("Ingrese la fecha de hoy:")
dia = int(input())
mes = int(input())
anio = int(input())
if dia <30:
    dia += 1
else:
   dia = 1
    if mes <12:
        mes += 1
    else:
     mes = 1
      anio += 1
print(dia, mes, anio)
    
    
