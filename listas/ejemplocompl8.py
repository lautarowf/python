# -*- coding: utf-8 -*-
# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento8: SEPARAR NÚMEROS PARES E IMPARES DE UN VECTOR")
print("-------------------------------------------------------")

# Inicialización: Crear un vector vacío para almacenar los números
vector_principal = []

# Entrada: Leer la dimensión del vector (cantidad de números a ingresar)
print("Ingrese la cantidad de números que tendrá el vector (máximo 100): ")
tamanio_vector = int(input())

# Crear dos vectores del mismo tamaño inicializados con ceros
vector_pares = [0] * tamanio_vector
vector_impares = [0] * tamanio_vector

# Entrada: Leer los números y cargarlos en el vector principal
print(f"Ingrese los {tamanio_vector} números del vector:")

for posicion in range(tamanio_vector):
    numero_usuario = int(input(f"Ingrese el número {posicion + 1}: "))
    vector_principal.append(numero_usuario)

# Inicialización de contadores:
contador_pares = 0     # Cuenta cuántos números pares se encontraron
contador_impares = 0   # Cuenta cuántos números impares se encontraron

# Proceso: Separar números en pares e impares
for posicion in range(tamanio_vector):
    numero_actual = vector_principal[posicion]
    
    if numero_actual % 2 == 0:
        # Es par: se almacena en el vector de pares
        vector_pares[contador_pares] = numero_actual
        contador_pares += 1
    else:
        # Es impar: se almacena en el vector de impares
        vector_impares[contador_impares] = numero_actual
        contador_impares += 1

# Salida: Mostrar los vectores de pares e impares (solo los valores válidos)
print("\nVector de números pares:")
print(vector_pares[0:contador_pares])  # Solo mostrar hasta la cantidad real de pares
print(f"El vector de pares tiene {contador_pares} elemento(s).")

print("\nVector de números impares:")
print(vector_impares[0:contador_impares])  # Solo mostrar hasta la cantidad real de impares
print(f"El vector de impares tiene {contador_impares} elemento(s).")

# Comparación: Determinar cuál vector tiene más elementos
if contador_pares > contador_impares:
    print("\nEl vector de pares tiene más elementos.")
elif contador_impares > contador_pares:
    print("\nEl vector de impares tiene más elementos.")
else:
    print("\nAmbos vectores tienen la misma cantidad de elementos.")
