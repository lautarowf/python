# Decoración: Título del Algoritmo
print("-------------------------------------------------------")
print("Complemento1: CONTAR NÚMEROS PARES.")
print("-------------------------------------------------------")

# Inicializar contador
cantidad_pares = 0

# Proceso
print("Ingrese 10 números:")

for numero_ingresado in range(1, 11):
    numero = int(input(f"Ingrese el número {numero_ingresado}: "))

    if numero % 2 == 0:
        cantidad_pares += 1  # Es par, sumamos 1 al contador

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")
print("Hay", cantidad_pares, "números pares.")
