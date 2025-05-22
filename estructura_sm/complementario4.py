#calcular el dia siguiente
print("Ingrese la fecha de hoy:")
dia = int(input())
mes = int(input())
anio = int(input())
if dia > 0 and dia <30:
    print(dia+1, "/", mes, "/", anio)
elif mes >0 and mes <12:
    print(1, "/", mes+1, "/", anio)
else:
    print(1, "/", 1, "/", anio+1)
    
