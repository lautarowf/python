#calcular el dia siguiente
print("Ingrese la fecha de hoy:")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

if mes == 2:
   if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
     dias_en_mes = 29
   else:
     dias_en_mes = 28
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
   dias_en_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
   dias_en_mes = 30
if dia <dias_en_mes:
    dia += 1
else:
    dia = 1 
    if mes <12:
        mes += 1
    else:
        mes = 1
        anio += 1
print(dia, mes, anio)