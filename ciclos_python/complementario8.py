# Lista con los nombres de los días de la semana
nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Lista para registrar los minutos de actividad de cada día
minutos_por_dia = []

# Variable para acumular el total de minutos semanales
total_minutos = 0

# Registrar los minutos por día
for dia in nombres_dias:
    minutos = int(input(f"Ingrese los minutos de actividad física del día {dia}: "))
    minutos_por_dia.append(minutos)
    total_minutos += minutos

# Calcular promedio semanal
promedio_semanal = total_minutos / 7

# Determinar el día con mayor y menor actividad
minutos_maximos = max(minutos_por_dia)
minutos_minimos = min(minutos_por_dia)
indice_maximo = minutos_por_dia.index(minutos_maximos)
indice_minimo = minutos_por_dia.index(minutos_minimos)
dia_mas_activo = nombres_dias[indice_maximo]
dia_menos_activo = nombres_dias[indice_minimo]

# Mostrar resultados
print("\n--- Resumen de actividad física ---")
print(f"Promedio semanal: {promedio_semanal:.2f} minutos por día")
print(f"Día con más actividad: {dia_mas_activo} ({minutos_maximos} minutos)")
print(f"Día con menos actividad: {dia_menos_activo} ({minutos_minimos} minutos)")
