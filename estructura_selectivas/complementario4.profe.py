print("--------------------------------------------------------------")
print("Ejercicio: DETERMINAR DÍA SIGUIENTE 2")
print("--------------------------------------------------------------")

# Entrada de datos
print("Ingrese la fecha de hoy:")
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

# Determinar si el año es bisiesto
bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

# Determinar el número de días del mes actual
if mes == 2:
    dias_del_mes = 29 if bisiesto else 28
elif mes in [4, 6, 9, 11]:
    dias_del_mes = 30
else:
    dias_del_mes = 31

# Calcular el día siguiente
if dia < dias_del_mes:
    dia += 1
else:
    dia = 1
    if mes == 12:
        mes = 1
        año += 1
    else:
        mes += 1

# Salida
print("Mañana va a ser:", dia, mes, año)