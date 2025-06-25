print("Seguimiento de hábitos saludables")
print("Ingrese cuántos vasos de agua tomó cada día (durante 7 días):")

# Inicialización
consumo = 0
consumoTotal = 0
contador = 0

# Registro de 7 días
while contador < 7:
    consumo = int(input(f"Día {contador + 1}: "))
    consumoTotal += consumo
    contador += 1

# Cálculo de promedio
promedio = consumoTotal / 7
print("Promedio diario:", promedio)

# Recomendación
if promedio < 8:
    print("💧 Se recomienda aumentar el consumo de agua.")
