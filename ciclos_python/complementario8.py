# Lista con los nombres de los días
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Lista vacía para guardar los minutos por día
minutos_por_dia = []

# Acumulador para la suma total
suma_total = 0

# Bucle for que recorre cada día
for dia in dias:
    minutos = int(input(f"Ingrese los minutos de actividad del día {dia}: "))
    minutos_por_dia.append(minutos)  # Agrega el dato a la lista
    suma_total += minutos  # Suma al total

# Cálculo del promedio
promedio = suma_total / 7

# Buscar el valor máximo y mínimo en la lista
maximo = max(minutos_por_dia)
minimo = min(minutos_por_dia)

# Buscar la posición (índice) donde se encuentra ese valor
indice_max = minutos_por_dia.index(maximo)
indice_min = minutos_por_dia.index(minimo)

# Mostrar resultados
print(f"Promedio semanal: {promedio:.2f} minutos")
print(f"Día con mayor actividad: {indice_max}")
print(f"Día con menor actividad: {indice_min}")