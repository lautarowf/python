#calcular el dia siguiente
print("Ingrese la fecha de hoy:")
dia = int(input())
mes = int(input())
anio = int(input())
if dia > 0 and dia <30:
    dia+1
    print(dia, "/", mes, "/", anio)
    
