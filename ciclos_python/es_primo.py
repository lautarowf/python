# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento7: DETERMINAR SI UN NÚMERO ES PRIMO.")
print("-------------------------------------------------------")

# Entrada
numero = int(input("Ingrese un número: "))

# Inicialización
tiene_divisores = 0  # Contador de divisores distintos de 1 y él mismo

# Proceso: verificar si tiene divisores entre 2 y numero-1
for posible_divisor in range(2, numero):
    if numero % posible_divisor == 0:
        tiene_divisores += 1

# Salida
print("\nSALIDA:")
print("-------------------------------------------------------")

if tiene_divisores == 0:
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
