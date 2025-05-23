#calcular el dia siguiente
print("Ingrese la fecha de hoy:")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))
if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
    if dia < 31:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            dia +=1
            print(dia, mes, anio)
    else:
        dia = 1
        mes +=1
        print(dia,mes,anio)
elif dia < 30:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dia +=1
            print(dia, mes, anio)
        else:
            dia = 1
            mes +=1
            print(dia,mes,anio)             
