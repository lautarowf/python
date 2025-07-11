# -*- coding: utf-8 -*-
# Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Complemento7: INSERTAR VALOR Y ORDENAR VECTOR ASCENDENTE")
print("-------------------------------------------------------")

# Inicialización: Crear un vector vacío donde se guardarán los números
vector_numeros = []

# Entrada: Leer 10 números y agregarlos al vector
print("Ingrese los 10 números del vector (no importa si están ordenados o no):")
for posicion_actual in range(10):
    numero_usuario = int(input(f"Ingrese el número {posicion_actual + 1}: "))
    vector_numeros.append(numero_usuario)

# Entrada: Leer el número adicional a insertar en el vector
numero_a_insertar = int(input("Ingrese el número adicional a insertar: "))

# Insertamos el nuevo número al final del vector
vector_numeros.append(numero_a_insertar)

# Proceso: Ordenar el vector completo de forma ascendente
# Se utilizará un ordenamiento basado en comparación e intercambio (no es burbuja clásica)

cantidad_elementos = len(vector_numeros)  # En este caso, 11 números

# Bucle externo: recorre cada posición del vector
for indice_externo in range(cantidad_elementos):
    # Bucle interno: compara la posición actual con todas las demás posiciones
    for indice_interno in range(cantidad_elementos):
        
        # En cada paso se comparan los valores de dos posiciones diferentes:
        # Si el valor en la posición interna es mayor que el valor en la posición externa,
        # entonces estos dos valores están desordenados y deben ser intercambiados.
        if vector_numeros[indice_interno] > vector_numeros[indice_externo]:
            
            # Intercambio de los dos valores usando una variable temporal
            valor_temporal = vector_numeros[indice_interno]
            vector_numeros[indice_interno] = vector_numeros[indice_externo]
            vector_numeros[indice_externo] = valor_temporal

            # En este punto los dos valores cambiaron de lugar para acercarse al orden correcto.

# Salida: Mostrar el vector ya ordenado de forma ascendente
print("\nVector ordenado en forma ascendente:")
for numero_actual in vector_numeros:
    print(numero_actual)