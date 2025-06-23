print("-------------------------------------------------------")
print("Complemento5: CALCULAR SUMA DE SERIE 2.")
print("-------------------------------------------------------")

# Inicialización
suma = 0

# Entrada
print("Ingrese número de términos:")
num_terminos = int(input())

# Proceso
for indice in range(1, num_terminos + 1):
    if indice % 2 == 0:
        suma = suma - (1 / indice)  # Para índices pares resto
    else:
        suma = suma + (1 / indice)  # Para índices impares sumo

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print("La suma será:", suma)
