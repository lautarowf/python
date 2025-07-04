dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
minutos_por_dia = []
suma_total = 0
for dia in dias:
    minutos = int(input(f"Ingrese los minutos de actividad del día {dia}: "))
    minutos_por_dia.append(minutos) 
    suma_total += minutos  
promedio = suma_total / 7
maximo = max(minutos_por_dia)
minimo = min(minutos_por_dia)
indice_max = minutos_por_dia.index(maximo)
indice_min = minutos_por_dia.index(minimo)
print(f"Promedio semanal: {promedio} minutos")
print(f"Día con mayor actividad: {indice_max}")
print(f"Día con menor actividad: {indice_min}")