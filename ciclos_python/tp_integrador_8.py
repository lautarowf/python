contador = 0
minutosTotales = 0

print("Registro de ejercicio semanal")
print("Ingrese cuántos minutos se ejercitó cada día:")

while contador < 7:
    minutos = int(input(f"Día {contador + 1}: "))
    minutosTotales += minutos
    contador += 1

promedio = minutosTotales / 7

print("\nPromedio diario de ejercicio:", promedio, "minutos")

if promedio < 30:
    print("💡 Te sugiero aumentar la actividad física.")
