#calcular el dia siguiente
print("Ingrese la fecha de hoy:")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))
if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if dia <31:
        dia += 1
    else:
        dia = 1 
        if mes <12:
            mes += 1
        else:
            mes = 1
            anio += 1
print(dia, mes, anio)
if mes == 4 or 6 or 9 or 11:
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
if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
    if mes == 2:
        if dia <29:
            dia += 1
        else:
            dia = 1 
            if mes <12:
                mes += 1
            else:
                mes = 1
                anio += 1
print(dia, mes, anio)