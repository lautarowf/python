# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento4: CALCULAR SUMA DE SERIE.")
print("-------------------------------------------------------")

# Entrada
print("Ingrese el número de términos: ")
cantidad_terminos = int(input())

# Inicialización
termino_actual = 5  # Vamos a sumar 5 antes de cada término, así el primero es 10
suma_total = 0      # Acumulador para la suma

# Proceso: Generar y sumar cada término
for contador in range(1, cantidad_terminos + 1):
    termino_actual += 5         # Aumenta de 5 en 5: 10, 15, 20...
    suma_total += termino_actual

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print("La suma de la serie es:", suma_total)
